//SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;
contract NeFiBoostManager is Ownable {
    string public constant name = "NebulaProtoStarManager";
    string public constant symbol = "PMGR";
    using SafeMath for uint256;
    using SafeMath for uint;
    struct PROTOstars {
	string name;
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
    mapping(address => PROTOstars[]) public protostars;
    mapping(address => TIMES[]) public nftTimes;
    address[] public PROTOaccounts;
    address[] public Managers;
    uint256[] public nftsHeld;
    uint256 public Zero = 0;
    uint256 public one = 1;
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
    protoManager public protoMGR;
    address public nftAddress;
    address public _protoManager;
    address payable public treasury;
    modifier managerOnly() {require(nebuLib.addressInList(Managers,msg.sender)== true); _;}
    modifier onlyGuard() {require(owner() == _msgSender() || Guard == _msgSender() || nebuLib.addressInList(Managers,_msgSender()) == true, "NOT_proto_GUARD");_;}
//ADDProtoStarRewards---------------------------------------------------------------------------------------------------------------------------------------------------
   function addProto(address _account, string memory _name) external {
    }
//COLLAPSEprotos--------------------------------------------------------------------------------------------------------------------------------------------------------
    function collapseProto(address _account, string memory _name) external{
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
    function updateprotoManager(address _account) external onlyGuard(){
    	INTupdateprotoManager(_account);
    }
    function INTupdateprotoManager(address _account) internal{
    	_protoManager = _account;
    	protoMGR = protoManager(_protoManager);
    }
    function updateBoostManager(address _account) external onlyGuard(){
    	INTupdateBoostManager(_account);
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
    function updateTeamPool(address _account) external onlyGuard(){
    	INTupdateTeamPool(_account);
    }
    function INTupdateTeamPool(address _account) internal{
        	teamPool = _account;
        }
    function updateRewardsPool(address _account) external onlyGuard(){
    	INTupdateRewardsPool(_account);
    }
    function INTupdateRewardsPool(address _account) internal{
        	rewardsPool = _account;
        }
    function updateGuard(address newVal) external onlyOwner(){
        Guard = newVal; //token swap address
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