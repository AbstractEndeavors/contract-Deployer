//SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;
contract NeFiBoostManager is Ownable {
    string public constant name = "NebulaProtoStarManager";
    string public constant symbol = "PMGR";
    using SafeMath for uint256;
    using SafeMath for uint;
    struct PROTOstars {
	string name;
	uint256 creationTime;
	uint256 lastClaimTime;
	uint256 protoElapsed;
	uint256 protoLife;
	uint256 lifeDecrease;
	uint256 collapseDate;
	bool insolvent;
    }
    struct DEADStars {
	string name;
	uint256 creationTime;
	uint256 lastClaimTime;
	uint256 protoElapsed;
	uint256 collapseDate;
	bool insolvent;
	bool imploded;
    	}
    struct PENDING{
    	uint256 calcTime;
    	uint256 boostRewardsMin;
    	uint256 lifeDecrease;
    	uint256 rewards;
	uint256 tempBoost;
	uint256 tempTotRewards;
	uint256 elapsed;
	uint256 boostElapsed;
    }
    struct TIMES {
	uint256 boostRewardsMin;
	uint256 rewardsMin;
	uint256 timeBoost;
	uint256 timeRegular;
	uint256 cashoutFeeRegular;
	uint256 cashoutFee;
	uint256 lifeDecrease;
	uint256 tempRewards;
	uint256 tempBoost;
	uint256 tempTotRewards;
    }
    mapping(address => PROTOstars[]) public protostars;
    mapping(address => DEADStars[]) public deadstars;
    mapping(address => TIMES[]) public nftTimes;
    mapping(address => PENDING[]) public pending;
    address[] public PROTOaccounts;
    address[] public PROTOtransfered;
    address[] public Managers;
    uint256[] public nftsHeld;
    uint256 public Zero = 0;
    uint256 public one = 1;
    uint256 public gas = 1*(10**17);
    uint256 public protoLife = 500 days;
    uint256 public claimFee;
    uint256 public rewardsPerMin;
    uint256[] public boostmultiplier;
    uint256[] public boostRewardsPerMin;
    uint256[] public cashoutRed;
    uint256[] public times;
    address Guard;
    bool public fees = false;
    overseer public over;
    feeManager public feeMGR;
    address public nftAddress;
    address payable public treasury;
    modifier managerOnly() {require(nebuLib.addressInList(Managers,msg.sender)== true); _;}
    modifier onlyGuard() {require(owner() == _msgSender() || Guard == _msgSender() || nebuLib.addressInList(Managers,_msgSender()) == true, "NOT_proto_GUARD");_;}
    constructor(address overseer_ ,address _feeManager, address payable _treasury ) {
    	over = overseer(overseer_);
	treasury = _treasury;
	feeMGR = feeManager(_feeManager);
	Managers.push(owner());
	rewardsPerMin = over.getRewardsPerMin();
	for(uint i=0;i<4;i++){
		boostmultiplier.push(over.getMultiplier(i));
		rewardsperMin = over.getRewardsPerMin;
		boostRewardsPerMin.push(boostRewardsPerMin(i));
		cashoutRed.push(over.getCashoutRed(i));
	}
    }
   function getTimes(address _account, uint256 _time, uint256 _id,uint256 calcTime,uint _x) internal returns (uint256,uint256){
   	uint256 nfTtime = over.getNftTimes(_account,_id,i);
   	uint256 elapsed = _time.sub(calcTime);
   	if(isLower(calcTime,nfTtime)==true){
   		uint256 nftElapsed = (nfTtime).sub(calcTime);
   		uint256 regElapsed = elapsed.sub(nftElapsed);
   		uint256 boostedElapsed = nebuLib.doPercentage(nftElapsed,boostmultiplier[i]);
   		uint256 totalElapsed = claimElapsed.add(boostElapsed);
   	        uint256 rewards = totalElapsed.mul(rewardsperMin);
   	        nftTimes[_account][_x].rewards = rewards;
   	        uint256 boostRewards = nebuLib.doPercentage(nftElapsed,boostRewardsPerMin[i]);
   	        uint256  totalRewards = rewards.add(boostRewards);
   	        pending[_account][_x].nftelapsed += nftElapsed;
	   	pending[_account][_x].boostElapsed += boostedElapsed;
	   	pending[_account][_x].boostedElapsed += totalElapsed;
	   	pending[_account][_x].boostRewards += boostRewards;
	   	pending[_account][_x].totalRewards = totalRewards;
   	}else{
   		uint256 nftElapsed = elapsed;
   	        uint256 boostedElapsed = nebuLib.doPercentage(nftElapsed,boostmultiplier[i]);
   		uint256 boostRewards = nebuLib.doPercentage(nftElapsed,boostRewardsPerMin[i]);
   		uint256 totalElapsed = claimElapsed.add(boostElapsed);
   		uint256 totalRewards = rewards.add(boostRewards);
   		pending[_account][_x].nftelapsed += nftElapsed;
	   	pending[_account][_x].boostElapsed += boostedElapsed;
	   	pending[_account][_x].boostedElapsed += totalElapsed;
	   	pending[_account][_x].boostRewards += boostRewards;
	   	pending[_account][_x].totalRewards = totalRewards;
   	}
   	}
   function queryBoost(address _account,uint256 _x) internal{
   	uint256 _time = block.timeStamp;
   	uint256 lastClaim = protostars[_account][_x].lastClaimTime;
   	uint256 calcTime = nftTimes[_account][count].calcTime;
   	uint256 allCount;
   	uint256 totalRew;
   	uint256 boostmul;
   	uint256 nftAmt;
   	if (over.isStaked(_account)==true){
	   	doPercentage(_x,perc);
	   	boostmul = boostmultiplier(_x);
	   	for(uint j=0;j<3;j++){
	   		_id = j;
	   		nftAmt = over.getNftAmount(_account,_id);
		   	for(uint i=0;i<nftAmt;i++){
		   		for(uint k=0;k<5;k++){
		   			getTimes(_account,_time,_id,k,calcTime,count);
	   				allCount +=1;
	   			}
	   		}
	   	}
	}
	uint256 totalElapsed;
	uint256 rewards;
	for(uint _x= allCount;_X<protos.length;_X++){
		totalElapsed = _time.sub(calcTime);
		rewards = totalElapsed.mul(rewardsperMin);
		pending[_account][_x].totalElapsed += totalElapsed;
		pending[_account][_x].rewards += rewards;
		pending[_account][_x].totalRewards += totalRewards;
	}
	pending[_account][count].calcTime = _time;
    }
    function claimBoost(address _account,uint256 _x) external{
    	queryBoost(_account);
    	nftTimes[_account][_x].lastClaimTime = pending[_account][count].calcTime;
    	uint256 totalRew;
	for(uint _x=0;_x<	protos.length;_X++){
		nftTimes[_account][_x].nftelapsed += pending[_account][_x].nftelapsed;
	   	nftTimes[_account][_x].boostElapsed += pending[_account][_x].boostElapsed;
	   	nftTimes[_account][_x].boostedElapsed += pending[_account][_x].boostedElapsed;
	   	nftTimes[_account][_x].boostRewards += pending[_account][_x].boostRewards;
	   	nftTimes[_account][_x].totalRewards = pending[_account][_x].totalRewards;
	   	nftTimes[_account][_x].totalElapsed += pending[_account][_x].totalElapsed;
		nftTimes[_account][_x].rewards += pending[_account][_x].rewards;
		nftTimes[_account][_x].totalRewards += pending[_account][_x].totalRewards;
		totalRew += pending[_account][_x].totalRewards;
	}
	ZeroPending(_account);
	totalRew;
   }
   function recProtoRewards(address _account) external onlyGuard{
   	PROTOstars[] storage stars = protostars[_account];
   	TIMES[] storage times = nftTimes[_account];
   	for(uint i=0;i<stars.length;i++){
	   	PROTOstars storage star = stars[i];
	   	TIMES storage time = times[i];
	   	star.lastClaimTime = star.lastClaimTime;
	   	star.protoElapsed =star.lastClaimTime - star.creationTime;
	   	star.rewards += time.tempRewards;
	   	star.lifeDecrease += time.lifeDecrease;
	   	star.boost += time.tempBoost;
	   	star.collapseDate = star.protoLife - star.lifeDecrease - star.protoElapsed;
  	}
  }
   function addProto(address _account, string memory _name) external onlyGuard  {
   	require(bytes(_name).length > 3 && bytes(_name).length < 32,"the Node name must be within 3 and 32 characters");
   	require(nameExists(_account,_name) == false,"name has already been used");
       	if (nebuLib.addressInList(PROTOaccounts,_account) == false){
	    	PROTOaccounts.push(_account);
	    }
    	PROTOstars[] storage protos = protostars[_account];
	uint256 _time = block.timestamp;
	uint256 collapse = _time.add(protoLife);
	protos.push(PROTOstars({
		name:_name,
		creationTime:_time,
		lastClaimTime:_time,
		protoElapsed:Zero,
		protoLife:protoLife,
		collapseDate:collapse,
		insolvent:false
	}));
	}
    function nameExists(address _account, string memory _name) internal view returns(bool){
    		PROTOstars[] storage protos = protostars[_account];
    	    	for(uint i = 0;i<protos.length;i++) {
    			PROTOstars storage proto = protos[i];
    			string memory name = proto.name;
    			if(keccak256(bytes(name)) == keccak256(bytes(_name))){
    				return true;
    			}
    		}
    		return false;
    }
    function findFromName(address _account, string memory _name) internal view returns(uint256){
    	    	PROTOstars[] storage protos = protostars[_account];
    	    	for(uint i = 0;i<protos.length;i++) {
    			PROTOstars storage proto = protos[i];
    			if(keccak256(bytes(proto.name)) == keccak256(bytes(_name))){
    				return i;
    			}
    		}
    }
    function changeFeeManager(address _address) external onlyGuard {
        address _feeManager = _address;
    	feeMGR = feeManager(_feeManager);
    }
    function changeName(string memory _name,string memory new_name) external {
    	address _account = msg.sender;
    	require(nameExists(_account,_name) == true,"name does not exists");
    	require(nebuLib.addressInList(PROTOaccounts,_account) == true,"you do not hold any Protostars Currently");
    	PROTOstars[] storage protos = protostars[_account];
    	PROTOstars storage proto = protos[findFromName(_account,_name)];
    	proto.name = new_name;
    	feeMGR.changeName(_name,new_name);
    }
    function getDeadStarsData(address _account, uint256 _x) external onlyGuard() returns(string memory,uint256,uint256,uint256,uint256,uint256,bool,bool){
    		DEADStars[] storage deads = deadstars[_account];
    		DEADStars storage dead = deads[_x];
    		return (dead.name,dead.creationTime,dead.lastClaimTime,dead.rewards,dead.boost,dead.collapseDate,dead.insolvent,dead.imploded);
    }
    function protoAccountData(address _account, uint256 _x) external onlyGuard() returns(string memory,uint256,uint256,uint256,uint256,uint256,uint256,uint256,uint256){
    		PROTOstars[] storage stars = protostars[_account];
    		PROTOstars storage star = stars[_x];
    		return (star.name,star.creationTime,star.lastClaimTime,star.protoElapsed,star.rewards,star.boost,star.protoLife,star.lifeDecrease,star.collapseDate);
    	}
   function protoAccountExists(address _account) external returns (bool) {
    	return nebuLib.addressInList(PROTOaccounts,_account);
    }
    function getCollapseDate(address _account,string memory _name) external view returns(uint256) {
       		PROTOstars[] storage stars = protostars[_account];
    		PROTOstars storage star = stars[findFromName(_account,_name)];
    		return star.collapseDate;
    }
    function getdeadStarsLength(address _account) external view returns(uint256){
    		DEADStars[] storage deads = deadstars[_account];
        	return deads.length;
    }
    function getProtoAccountsLength() external view returns(uint256){
    	return PROTOaccounts.length;
    }
    function getProtoAddress(uint256 _x) external view returns(address){
    	return PROTOaccounts[_x];
    }
    function getProtoStarsLength(address _account) external view returns(uint256){
    	PROTOstars[] storage stars = protostars[_account];
    	return stars.length;
    }
    function updateTreasury(address payable _treasury) external onlyOwner() {
    	treasury = _treasury;
    }
    function updateFeeManager(address _feeManager) external onlyGuard(){
    		feeMGR = feeManager(_feeManager);
    }
    function updateRewardsPerMin() external onlyGuard() {
    	rewardsPerMin = over.getRewardsPerMin();
	for(uint i=0;i<3;i++){
		boostRewardsPerMin[i] = over.getBoostPerMin(i);
	}
    }
    function updateGuard(address newVal) external onlyOwner {
        Guard = newVal; //token swap address
    }
    function updateManagers(address newVal) external onlyOwner {
    	if(nebuLib.addressInList(Managers,newVal) ==false){
        	Managers.push(newVal); //token swap address
        }
    }
}