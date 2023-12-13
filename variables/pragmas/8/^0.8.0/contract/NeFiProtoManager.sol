//SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;
contract NeFiProtoManager is Ownable {
    string public constant name = "NebulaProtoStarManager";
    string public constant symbol = "PMGR";
    using SafeMath for uint256;
    using SafeMath for uint;
    struct PROTOstars {
	string name;
	uint256 creationTime;
	uint256 lastClaimTime;
	uint256 lifeDecrease;
	uint256 protoElapsed;
	uint256 collapseDate;
	bool insolvent;
	bool imploded;
	bool collapsed;
    }
    struct DEADStars {
	string name;
	uint256 creationTime;
	uint256 lastClaimTime;
	uint256 lifeDecrease;
	uint256 protoElapsed;
	uint256 collapseDate;
	bool insolvent;
	bool imploded;
	bool collapsed;
    	}
    mapping(address => PROTOstars[]) public protostars;
    mapping(address => DEADStars[]) public deadstars;
    address[] public PROTOaccounts;
    address[] public PROTOtransfered;
    address[] public DeadStars;
    address[] public Managers;
    uint256[] public nftsHeld;
    uint256 public Zero = 0;
    uint256 public one = 1;
    uint256 public claimFee;
    uint256 public protoLife = 500 days;
    uint256 public rewardsPerMin;
    uint256[] public boostmultiplier;
    uint256[] public boostRewardsPerMin;
    address public _feeManager;
    address public _dropManager;
    address public _boostManager;
    address public _overseer;
    address public _updateManager;
    address payable treasury;
    address public NeFiToken;
    address public feeToken;
    uint256[] public cashoutRed;
    uint256[] public times;
    address Guard;
    bool public fees = false;
    overseer public over;
    boostManager public boostMGR;
    feeManager public feeMGR;
    dropManager public dropMGR;
    NeFiUpdateManager public updateMGR;
    address public nftAddress;
    address payable public treasury;
    modifier managerOnly() {require(NeFiLib.addressInList(Managers,msg.sender)== true || _msgSender() == owner()); _;}
    modifier onlyGuard() {require(_msgSender() == _feeManager || _msgSender() == _dropManager || _msgSender() == owner() || _msgSender() == _updateManager, "NOT_proto_GUARD");_;}
    constructor(address updatemanager) {
    	_updateManager = updatemanager;
    	updateMGR = updateManager(_updateManager);
    	INTupdateFeeToken(updateMGR.getFeeToken);
    	INTupdateTreasury(updateMGR.getTreasury);
    	INTupdateOverseer(updateMGR.getOverseer);
    	INTupdateDropManager(updateMGR.getDropManager);
    	INTupdateFeeManager(updateMGR.getFeeManager);
    	INTupdateBoostManager(updateMGR.getBoostManager);
	Managers.push(owner());
	rewardsPerMin = over.getRewardsPerMin();
	for(uint i=0;i<3;i++){
		boostmultiplier.push(over.getMultiplier(i));
		boostRewardsPerMin.push(over.getRewardsPerMin());
		cashoutRed.push(over.getCashoutRed(i));
	}
    }
//nameProtos----------------------------------------------------------------------------------------------------------------------------
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
    function changeName(address _account, string memory _name,string memory new_name) external {
    	address _account = msg.sender;
    	require(nameExists(_account,_name) == true,"name does not exists");
    	require(NeFiLib.addressInList(PROTOaccounts,_account) == true,"you do not hold any Protostars Currently");
    	PROTOstars[] storage protos = protostars[_account];
    	PROTOstars storage proto = protos[findFromName(_account,_name)];
    	proto.name = new_name;
    	feeMGR.updateName(_account,_name,new_name);
    	boostMGR.updateName(_account,_name,new_name);
    }
//CreateStars-----------------------------------------------------------------------------------------------------------------------------------
   function addProto(address _account,string memory _name) external onlyGuard(){
		INTaddProto(_account,_name);
	}
   function INTaddProto(address _account,string memory _name) internal{
   	require(bytes(_name).length > 3 && bytes(_name).length < 32,"the Node name must be within 3 and 32 characters");
   	require(nameExists(_account,_name) == false,"name has already been used");
       	if (NeFiLib.addressInList(PROTOaccounts,_account) == false){
	    	PROTOaccounts.push(_account);
	    }
    	PROTOstars[] storage protos = protostars[_account];
    	uint256 _time = block.timestamp;
    	uint256 collapse = _time.add(protoLife);
    	protos.push(PROTOstars({
    	    name:_name,
    	    creationTime:_time,
    	    lastClaimTime:_time,
    	    lifeDecrease:Zero,
    	    protoElapsed:Zero,
    	    collapseDate:block.timestamp.add(protoLife),
    	    insolvent:false,
    	    imploded:false,
    	    collapsed:true
    	    }));
    	    feeMGR.addProto(_account,_name);
    	    boostMGR.addProto(_account,_name);
    	  }
//getStarsData-----------------------------------------------------------------------------------------------------------
    function protoAccountExists(address _account) external returns (bool) {
    	return NeFiLib.addressInList(PROTOaccounts,_account);
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
    function protoAccountData(address _account, uint256 _x) external onlyGuard() returns(string memory,uint256,uint256,uint256,uint256,uint256){
    		PROTOstars[] storage stars = protostars[_account];
    		PROTOstars storage star = stars[_x];
    		return (star.name,star.creationTime,star.lastClaimTime,star.protoElapsed,star.lifeDecrease,star.collapseDate);
    	}
//deadStars--------------------------------------------------------------------------------------------------------------
    function collapseProto(address _account, uint256 _x,bool _bool) external onlyFeeManager() {
    	protostars[_account][_x].collapsed = _bool;
    	if(_bool == true){
    		INTcollapseProto(_account,_x);
    	}
    }
    function implodedProto(address _account, uint256 _x,bool _bool) external onlyFeeManager() {
    	protostars[_account][_x].imploded = _bool;
    	if(_bool == true){
    		INTcollapseProto(_account,_x);
    	}
    }
    function InsolventProto(address _account, uint256 _x,bool _bool) external onlyFeeManager() {
    	protostars[_account][_x].insolvent = _bool;
    }
    function INTcollapseProto(address _account, uint256 _x) internal {
    	PROTOstars[] storage protos = protostars[_account];
    	PROTOstars storage proto = protos[_x];
	boostMGR.collapseProto(_account,proto.name);
    	feeMGR.collapseProto(_account,proto.name);
    	boostMGR.collapseProto(_account,proto.name);
    	DEADStars[] storage dead = deadstars[_account];
    	(bool owed,bool insolvent,bool imploded, bool collapsed) = feeMGR.getBool(_account,_x);
    	dead.push(DEADStars({
    	    name:proto.name,
    	    creationTime:proto.creationTime,
    	    lastClaimTime:proto.lastClaimTime,
    	    protoElapsed:proto.protoElapsed,
	    collapseDate:proto.collapseDate,
	    lifeDecrease:proto.lifeDecrease,
    	    insolvent:insolvent,
    	    imploded:imploded,
    	    collapsed:collapsed
    	    }));
    	for(uint i=_x;i<protos.length;i++){
    		if(i != protos.length-1){
  			PROTOstars storage proto_bef = protos[i];
    			PROTOstars storage proto_now = protos[i+1];
    			proto_bef.name=proto_now.name;
			proto_bef.creationTime=proto_now.creationTime;
			proto_bef.lastClaimTime=proto_now.lastClaimTime;
			proto_bef.protoElapsed=proto_now.protoElapsed;
			proto_bef.lifeDecrease=proto_now.lifeDecrease;
			proto_bef.collapseDate=proto_now.collapseDate;
			proto_bef.insolvent=proto_now.insolvent;
    		}
    	}
    	protos.pop();
    	if (NeFiLib.addressInList(DeadStars,_account) == false){
    		DeadStars.push(_account);
    	}
    }
//getDeadData-------------------------------------------------------------------------------------------------------------------------------------------
    function getDeadAccountsLength() external view returns(uint256){
    	return DeadStars.length;
    }
    function getDeadStarsLength(address _account) external view returns(uint256){
    		DEADStars[] storage deads = deadstars[_account];
        	return deads.length;
    }
    function getDeadStarsData(address _account, uint256 _x) external onlyGuard() returns(string memory,uint256,uint256,uint256,uint256,uint256,bool,bool,bool){
    		DEADStars[] storage deads = deadstars[_account];
    		DEADStars storage dead = deads[_x];
    		return (dead.name,dead.creationTime,dead.lastClaimTime,dead.lifeDecrease,dead.protoElapsed,dead.collapseDate,dead.imploded,dead.insolvent,dead.imploded);
    }
//changeWallets-----------------------------------------------------------------------------------------------
    function updateNeFiToken(address _account) external onlyGuard(){
    	INTupdateNeFiToken(_account);
    }
    function INTupdateNeFiToken(address _account) internal{
    	NeFiToken = _account;
    	NeFiTok = IERC20(NeFiToken);
    }
    function updateFeeToken(address _account) external onlyGuard(){
    	INTupdateFeeToken(_account);
    }
    function INTupdateFeeToken(address _account) internal{
    	feeToken = _account;
    	feeTok = IERC20(feeToken);
    }
    function updateOverseer(address _account) external onlyGuard(){
    	INTupdateOverseer(_account);
    }
    function INTupdateOverseer(address _account) internal{
    	_overseer = _account;
    	over = overseer(_overseer);
    }
    function updateDropManager(address _account) external onlyGuard(){
    	INTupdateDropManager(_account);
    }
    function INTupdateDropManager(address _account) internal{
    	_dropManager = _account;
    	dropMGR = dropManager(_dropManager);
    }
    function updateFeeManager(address _account) external onlyGuard(){
    	INTupdateFeeManager(_account);
    }
    function INTupdateFeeManager(address _account) internal{
    	_feeManager = _account;
    	feeMGR = feeManager(_feeManager);
    }
    function updateBoostManager(address _account) external onlyGuard(){
    	INTupdateBoostManager(address _account);
    }
    function INTupdateBoostManager(address _account) internal{
    	_boostManager = _account;
    	boostMGR = boostManager(_boostManager);
    }
    function updateTreasury(address payable _account) external onlyGuard(){
    	INTupdateTreasury(_account);
    }
    function INTupdateTreasury(address payable _account) internal{
    	treasury = _account;
    }
    function updateGuard(address newVal) external onlyOwner() {
        Guard = newVal; //token swap address
    }
    function updateManagers(address newVal) external onlyOwner() {
    	if(NeFiLib.addressInList(Managers,newVal) ==false){
        	Managers.push(newVal); //token swap address
        }
    }
//Overflow-----------------------------------------------------------------------------------------
    function transferOut(address payable _to,uint256 _amount) payable external  onlyOwner(){
		_to.transfer(_amount);
	}
    function transferAllOut(address payable _to,uint256 _amount) payable external onlyOwner(){
		_to.transfer(address(this).balance);
	}
    function sendAllTokenOut(address payable _to,address _token) external onlyOwner(){
		IERC20 newtok = IERC20(_token);
		newtok.transferFrom(address(this), _to, newtok.balanceOf(address(this)));
	}
}