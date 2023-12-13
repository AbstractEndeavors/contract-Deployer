//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract NeFiDropManager is Ownable{
	using SafeMath for uint256;
	struct DROPS{
		uint256 dropped;
		uint256 claimed;
		uint256 transfered;
		uint256 fees;
		uint256 remaining;
	}
	struct TRANSFERS{
		uint256 totalProtos;
		uint256 totalFees;
		uint256 transfered;
		uint256 totalClaims;
		uint256 totalDrops;
	}
	mapping(address => DROPS) public airdrop;
	mapping(address => TRANSFERS) public transfers;
	address[] public Managers;
	address[] public protoOwners;
	address[] public transfered;
	address payable treasury;
	uint256 gracePeriod = 5 days;
	uint256 feePeriod = 31 days;
	uint256 protoLife = 500 days;
	uint256 maxPayPeriods = 12;
	uint256 maxFeePayment = 365 days;
	bool avaxOff = false;
        bool tokOff = false;
        uint256 Zero = uint256(0);
        bool feeMGRpayOff = false;
	uint256 public tokFee = 15*(10**6);
	address oldDrop;
	address Guard;
	ProtoManager public protoMGR;
	protoMGR = ProtoManager(0xdb6933b9ef215bddd70b9d1fce230ce03a5a5ae7);
	dropManager public dropMGR;
	dropMGR = dropManager(0x35523fB3A015781039B9a2AA40FeE7aA1bd6d3f9);
	feeManager public feeMGR;
	overseer public over;
	IERC20 public feeTok;
	modifier managerOnly() {require(NeFiLib.addressInList(Managers,msg.sender)== true); _;}
	constructor(address[] memory addresses){
		feeMGR = feeManager(addresses[0]);
		over = overseer(addresses[1]);
		feeTok = IERC20(addresses[2]);
		treasury = payable(address(owner()));
		Managers.push(owner());
	}
	//toFeeMGR------------------------------------------------------------------------------------------------------------------
	//SpecFeesToken;
	function sendFeeTokenSpec(uint256 _intervals, uint256 _x) payable external{
		require(feeMGRpayOff == false, "sorry feeMGR pay is off currently");
		require(tokOff == false, "sorry Token Payments are currently disabled, please use AVAX");
		(address _account,uint256 needed, uint256 balanceRemainder,uint256 _intervals) = getVars(msg.sender,_intervals);
		(needed,_intervals) = checkAllowance(_account,checkIntervalsSpec(_account,_intervals,_x));
	        feeMGR.payFeeToken(_account,_intervals,_x,needed);
		if(msg.value > 0){
			payable(_account).transfer(msg.value);
		}
	}
    	//SpecFeesAvax
    	function payFeeAvaxSpec(uint256 _intervals,uint256 _x) payable external{
    		require(feeMGRpayOff == false, "sorry feeMGR pay if off currently");
    		require(avaxOff == false, "sorry AVAX Payments are currently disabled, please use USDC");
    		(address _account,uint256 needed, uint256 balanceRemainder,uint256 _intervals) = getVars(msg.sender,_intervals);
		(balanceRemainder,needed,_intervals) = checkAvaxSent(msg.value,checkIntervalsSpec(_account,_intervals,_x));
    		feeMGR.payFeeAvax{ value: needed }(_account,_intervals,_x);
    		if(balanceRemainder > 0){
			payable(_account).transfer(balanceRemainder);
		}
    	}
    	//FeesToken
	function sendFeeToken(uint256 _intervals) payable external {
    		require(feeMGRpayOff == false, "sorry feeMGR pay if off currently");
    		require(tokOff == false, "sorry Token Payments are currently disabled, please use AVAX");
		(address _account,uint256 needed, uint256 balanceRemainder,uint256 _intervals) = getVars(msg.sender,_intervals);
		(needed,_intervals) = checkAllowance(_account,checkIntervals(_account,_intervals));
	        feeMGR.payFeeToken(_account,_intervals,101,needed);
    		if(msg.value > 0){
			payable(_account).transfer(msg.value);
		}
    	}
	//FeesAvax
    	function sendFeeAvax(uint256 _intervals) payable external{
 		require(avaxOff == false, "sorry AVAX Payments are currently disabled, please use USDC");
 		require(avaxOff == false, "sorry AVAX Payments are currently disabled, please use USDC");
		(address _account,uint256 needed, uint256 balanceRemainder,uint256 _intervals) = getVars(msg.sender,_intervals);
		(balanceRemainder,needed,_intervals) = checkAvaxSent(msg.value,checkIntervals(_account,_intervals));
    		feeMGR.payFeeAvax{ value: needed }(_account,_intervals,101);
    		if(balanceRemainder > 0){
			payable(_account).transfer(balanceRemainder);
		}
    	}
    	//InHouse------------------------------------------------------------------------------------------------------------------
	//SpecFeesToken
	function protoFeesTokenSpec(uint256 _intervals,uint256 _x) payable external{
		require(tokOff == false, "sorry Token Payments are currently disabled, please use Avax");
		(address _account,uint256 needed, uint256 balanceRemainder,uint256 _intervals) = getVars(msg.sender,_intervals);
		(needed,_intervals) = checkAllowance(_account,checkIntervalsSpec(_account,_intervals,_x));
	    	feeMGR.MGRrecPayFees(_account,_intervals,_x);
	        feeTok.transferFrom(_account, treasury, needed);
	        if(msg.value > 0){
			payable(_account).transfer(msg.value);
		}
	}
	//FeesAvaxSpec
	function protoFeesAvaxSpec(uint256 _intervals,uint256 _x) payable external{
		require(avaxOff == false, "sorry AVAX Payments are currently disabled, please use USDC");
		(address _account,uint256 needed, uint256 balanceRemainder,uint256 _intervals) = getVars(msg.sender,_intervals);
		(balanceRemainder,needed,_intervals) = checkAvaxSent(msg.value,checkIntervalsSpec(_account,_intervals,_x));
	        feeMGR.MGRrecPayFees(_account,_intervals,_x);
	        treasury.transfer(needed);
	        if(balanceRemainder > 0){
			payable(_account).transfer(balanceRemainder);
		}
	}
	//FeesToken
	function protoFeesToken(uint256 _intervals) payable external{
		require(tokOff == false, "sorry Token Payments are currently disabled, please use AVAX");
		(address _account,uint256 needed, uint256 balanceRemainder,uint256 _intervals) = getVars(msg.sender,_intervals);
		(needed,_intervals) = checkAllowance(_account,checkIntervals(_account,_intervals));
		feeMGR.MGRrecPayFees(_account,_intervals,101);
	        feeTok.transferFrom(_account, treasury, needed);
	        if(msg.value > 0){
			payable(_account).transfer(msg.value);
		}
	}
	//FeesAvax
	function protoFeesAvax(uint256 _intervals) payable external{
		require(avaxOff == false, "sorry AVAX Payments are currently disabled, please use USDC");
		(address _account,uint256 needed, uint256 balanceRemainder,uint256 _intervals) = getVars(msg.sender,_intervals);
		(balanceRemainder,needed,_intervals) = checkAvaxSent(msg.value,checkIntervals(_account,_intervals));
		feeMGR.MGRrecPayFees(_account,_intervals,101);
	        treasury.transfer(needed);
	        if(balanceRemainder > 0){
			payable(_account).transfer(balanceRemainder);
		}
	}
	//ProtoClaim  ------------------------------------------------------------------------------------------------------------------------
	//ProtoClaimToken
    	function createProtoFeeTok(string memory _name) payable external{
    		require(tokOff == false, "sorry Token Payments are currently disabled, please use AVAX");
    		(address _account,uint256 needed, uint256 balanceRemainder,uint256 _intervals) = getVars(msg.sender,1);
		(needed,_intervals) = checkAllowance(_account,_intervals);
		checkProtoCreate(_account,_name);
	        feeTok.transferFrom(_account, treasury, needed);
	        if(msg.value > 0){
			payable(_account).transfer(msg.value);
		}
	}
	//ProtoClaimAvax
	function createProtoAvax(string memory _name) payable external {
		require(avaxOff == false, "sorry AVAX Payments are currently disabled, please use USDC");
		(address _account,uint256 needed, uint256 balanceRemainder,uint256 _intervals) = getVars(msg.sender,1);
		(balanceRemainder,needed,_intervals) = checkAvaxSent(msg.value,_intervals);
		checkProtoCreate(_account,_name);
		payable(treasury).transfer(needed);
		if(balanceRemainder > 0){
			payable(_account).transfer(balanceRemainder);
		}
	}
	//functions --------------------------------------------------------------------------------------------------
	function getVars(address _account,uint256 _intervals) public returns(address,uint256,uint256,uint256){
		return (_account,Zero,Zero,_intervals);
	}
	function checkIntervalsSpec(address _account,uint256 _intervals,uint256 _x) public returns(uint256){
		getInList(_account);
		if(getFeesPaid(_account)>0){
			uint256 payables = getTotalPayableSpec(_account,_x);
			require(payables >0,"you have no more fees to pay for this Proto");
			if(_intervals>payables){
				_intervals = payables;
			}
		}
		return _intervals;
	}
	function checkIntervals(address _account,uint256 _intervals) public returns(uint256){
		getInList(_account);
		if(getFeesPaid(_account)>0){
			uint256 payables = getTotalPayable(_account);
			require(payables >0,"you have no more fees to pay for this Proto");
			if(_intervals>payables){
				_intervals = payables;
			}
		}
		return _intervals;
	}
	function checkAvaxSent(uint256 _sent,uint256 _intervals) public returns(uint256,uint256,uint256){
		require(_intervals >0, "Doesnt Look Like you opted to pay any fees at this time");
		uint256 _needed = uint256(over.getFee()).mul(_intervals);
		require(_sent >= _needed, "Doesnt Look Like you sent enough to pay the fees at this time");
		uint256 _balanceRemainder = _sent.sub(_needed);
		return (_balanceRemainder,_needed,_intervals);
	}
	function checkProtoCreate(address _account,string memory _name) internal {
		require(getDropped(_account)>0,"you dont have any protos dropped to your account");
		require(getRemaining(_account)>0,"you have already claimed all of your protos");
		require(feeMGR.EXTnameExists(_account,_name)==false,"you have already used that name, please choose another");
		require(bytes(_name).length>3 ,"name is too small, under 32 characters but more than 3 please");
		require(bytes(_name).length<32 ,"name is too big, over 3 characters but under than 32 please");
		feeMGR.addProto(_account,_name);
		updateClaimed(_account);
	}
	function checkAllowance(address _account,uint256 _intervals) public returns (uint256,uint256) {
		require(_intervals >0, "Doesnt Look Like you opted to pay any fees at this time");
		uint256 _needed = tokFee.mul(_intervals);
		require(_needed <= feeTok.allowance(_account, address(this)), "Check the token allowance");
		require(_needed <= feeTok.allowance(_account, treasury), "Check the token allowance");
		require(_needed <= feeTok.balanceOf(_account), "you do not hold enough to pay the fees");
		return (_needed,_intervals);
	}
	function isFreeClaim(address _account) internal returns(bool){
		if(getClaimed(_account)<getFeesPaid(_account)){
			return true;
		}
		return false;
	}
	function getInList(address _account) internal{
		if(NeFiLib.addressInList(protoOwners,_account) ==false){
			protoOwners.push(_account);
		}
	}
	function getTotalPayableSpec(address _account,uint256 _x) internal returns(uint256){
		return feeMGR.getProtoTotalPayable(_account,_x);
	}
	function getTotalPayable(address _account) internal returns(uint256){
		return feeMGR.getTotalPayable(_account);
	}
	function getFeesPaid(address _account) internal returns(uint256){
		airdrop[_account].fees = feeMGR.getFeesPaid(_account);
		return airdrop[_account].fees;
	}
	function getDropped(address _account) internal returns(uint256){
		return airdrop[_account].dropped;
	}
	function getClaimed(address _account) internal returns(uint256){
		return airdrop[_account].claimed;
	}
	function getRemaining(address _account) internal returns(uint256){
		airdrop[_account].remaining = airdrop[_account].dropped - airdrop[_account].claimed;
		return airdrop[_account].remaining;
	}
	function updateDropped(address _account) internal returns(uint256){
		airdrop[_account].transfered;
	}
	function updateClaimed(address _account) internal{
		airdrop[_account].claimed +=1;
	}
	function EXTgetdropped(address _account) external returns(uint256){
		return airdrop[_account].transfered;
	}
	function EXTgetClaimed(address _account) external returns(uint256){
		return airdrop[_account].claimed;
	}
	function EXTgetRemaining(address _account) external returns(uint256){
		airdrop[_account].remaining = airdrop[_account].dropped - airdrop[_account].claimed;
		return airdrop[_account].remaining;
	}
	function EXTupdateDropped(address _account) external  returns(uint256)  {
		airdrop[_account].transfered +=1;
	}
	function EXTupdateClaimed(address _account) external  returns(uint256) {
		airdrop[_account].claimed +=1;
	}
	function addAirDrops(address[] memory _accounts,uint256[] memory _amounts,bool _neg,bool subTrans) external managerOnly() {
		for(uint i=0;i<_accounts.length;i++){
			DROPS storage drop = airdrop[_accounts[i]];
			if(_neg == false){
				drop.dropped += _amounts[i];
			}else{
				if(drop.dropped != 0){
						drop.dropped -= _amounts[i];
				}
			}
			if(subTrans==true){
				drop.dropped -= drop.transfered;
			}
		}
	}
	function createForAllFees(address[] memory adds,uint256[] memory strucNum) external onlyOwner{
		for(uint i=0;i<adds.length;i++){
			airdrop[adds[i]].fees = strucNum[i];
			feeMGR.MGRrecPayFees(adds[i],strucNum[i],101);
		}
	}
	function createForAllclaimed(address[] memory adds,uint256[] memory strucNum) external  onlyOwner{
		for(uint i=0;i<adds.length;i++){
			airdrop[adds[i]].claimed = strucNum[i];
		}
	}
	function createForAlltransfered(address[] memory adds,uint256[] memory strucNum) external onlyOwner{
		for(uint i=0;i<adds.length;i++){
			airdrop[adds[i]].transfered =strucNum[i];
		}
	}
	function createForAlldropped (address[] memory adds,uint256[] memory strucNum) external onlyOwner{
		for(uint i=0;i<adds.length;i++){
			airdrop[adds[i]].dropped = strucNum[i];
		}
	}
	function createForAlladd(address[] memory adds,string[] memory names) external  onlyOwner{
		for(uint i=0;i<adds.length;i++){
			feeMGR.addProto(adds[i],names[i]);
			updateClaimed(adds[i]);
		}
	}
	function MGRMAkeDrops(address[] memory _accounts,uint256[] memory _x) external onlyOwner{
		INTMGRMAkeDrops(_accounts,_x);
	}
	function INTMGRMAkeDrops(address[] memory _accounts,uint256[] memory _x) internal  {
		address _account;
		uint j = 0;
		uint k = 0;
		for(uint j = 0;j<_accounts.length;j++){
			_account = _accounts[j];
			airdrop[_account].dropped = _x[k];
			k +=1;
			airdrop[_account].claimed = _x[k];
			k +=1;
			airdrop[_account].transfered =_x[k];
			k +=1;
			airdrop[_account].fees= _x[k];
		}
	}
	function MGRMathDrops(address[] memory _accounts,uint256[] memory _x,bool[] memory _maths) external onlyOwner{
		address _account;
		uint j = 0;
		uint k = 0;
		for(uint j = 0;j<_accounts.length;j++){
			_account = _accounts[j];
			if(_maths[j] == true){
				airdrop[_account].dropped += _x[k];
				k +=1;
				airdrop[_account].claimed += _x[k];
				k +=1;
				airdrop[_account].transfered +=_x[k];
				k +=1;
				airdrop[_account].fees += _x[k];
			}else{
				airdrop[_account].dropped -= _x[k];
				k +=1;
				airdrop[_account].claimed -= _x[k];
				k +=1;
				airdrop[_account].transfered -=_x[k];
				k +=1;
				airdrop[_account].fees -= _x[k];
			}
		}
		if(NeFiLib.addressInList(transfered,_account) == false){
			protoOwners.push(_account);
			transfered.push(_account);
		}
	}
	function removeManagers(address newVal) external managerOnly() {
    		if(NeFiLib.addressInList(Managers,newVal) ==true){
    			uint _i = NeFiLib.isInList(Managers,newVal);
    			uint len = Managers.length-1;
    			Managers.push();
    			for(uint i=_i;i<len;i++){
    				uint _i_ = i +1;
    				Managers[i] = Managers[_i_];
    			}
    			Managers.pop();
        	}
    	}
    	function changeFeeTokenPrice(uint256 _tokFee) external onlyOwner{
    		tokFee = _tokFee;
        }
    	function turnfeeMGRpayOff(bool _feeOff) external onlyOwner{
    		feeMGRpayOff = _feeOff;
        }
    	function turnFeeTokOff(bool _tokOff) external onlyOwner{
    		tokOff = _tokOff;
        }
    	function changeturnAvaxOff(bool _avaxOff) external onlyOwner{
    		avaxOff = _avaxOff;
        }
    	function changeTreasury(address _account) external onlyOwner{
    		treasury = payable(_account);
        }
        function changeGuard(address _account) external onlyOwner{
    		Guard = _account;
        }
	function transferOut(address payable _to,uint256 _amount) payable external  onlyOwner{
		_to.transfer(_amount);
	}
	function sendTokenOut(address _to,address _token, uint256 _amount) external onlyOwner{
		IERC20 newtok = IERC20(_token);
		feeTok.transferFrom(address(this), _to, _amount);
	}
	function transferAllOut(address payable _to,uint256 _amount) payable external onlyOwner{
		_to.transfer(address(this).balance);
	}
	function sendAllTokenOut(address payable _to,address _token) external onlyOwner{
		IERC20 newtok = IERC20(_token);
		feeTok.transferFrom(address(this), _to, feeTok.balanceOf(address(this)));
	}
	function updateManagers(address newVal) external  onlyOwner{
    		if(NeFiLib.addressInList(Managers,newVal) ==false){
        		Managers.push(newVal); //token swap address
        	}
    	}
    	 function updatefeeManager(address newVal) external onlyOwner{
    		feeMGR = feeManager(newVal);
    	}
	function updateFeeToken(address newVal) external onlyOwner{
    		feeTok = IERC20(newVal);
    	}
    	function updateOverseer(address newVal) external onlyOwner{
    		over = overseer(newVal);
	}
    	receive() external payable onlyOwner{
            payable(msg.sender).transfer(msg.value);
        }
        fallback() external payable {}
}