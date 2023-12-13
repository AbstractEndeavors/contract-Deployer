//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract updateManager is Ownable {
	address public _feeManager;
	address public _protoManager;
	address public _dropManager;
	address public _boostManager;
	address public _overseer;
	address public teamPool;
	address public rewardsPool;
	address public payable(treasury);
	feeManager public feeMGR;
	boostManager public boostMGR;
	protoManager public protoMGR;
	dropManager public dropMGR;
	overseer public over;
//internalUpdate-----------------------------------------------------------------------------------------------------------
	function INTupdateFeeManager() internal{
		protoMGR.updateFeeManager(_feeManager);
		dropMGR.updateFeeManager(_feeManager);
		boostMGR.updateFeeManager(_feeManager);
	}
	function INTupdateProtoManager() internal{
		dropMGR.updateProtoManager(_protoManager);
		feeMGR.updateProtoManager(_protoManager);
		boostMGR.updateProtoManager(_protoManager);
	}
	function INTupdateDropManager() internal{
		protoMGR.updateDropManager(_dropManager);
		feeMGR.updateDropManager(_dropManager);
		boostMGR.updateDropManager(_dropManager);
	}
	function INTupdateBoostManager() internal{
		protoMGR.updateBoostManager(_boostManager);
		dropMGR.updateBoostManager(_boostManager);
		feeMGR.updateBoostManager(_boostManager);
	}
	function INTupdateTreasury() internal{
		protoMGR.updateTreasury(treasury);
		feeMGR.updateTreasury(treasury);
		boostMGR.updateTreasury(treasury);
		dropMGR.updateTreasury(treasury);
	}
	function INTupdateOverseer() internal{
		protoMGR.updateOverseer(_overseer);
		feeMGR.updateOverseer(_overseer);
		dropMGR.updateOverseer(_overseer);
		boostMGR.updateOverseer(_overseer);
	}
	function INTupdateRewardsPool() internal{
		feeMGR.updateRewardsPool(_rewardsPool);
	}
	function INTupdateTeamPool() internal{
		feeMGR.updateTeamPool(_TeamPool);
	}
//externalUpdate-----------------------------------------------------------------------------------------------------------
	function updateTreasury() external onlyOwner{
		INTupdateTreasury();
	}
	function updateBoostManager() external onlyOwner{
		INTupdateBoostManager();
	}
	function updateDropManager() external onlyOwner{
		INTupdateDropManager();
	}
	function updateProtoManager() external onlyOwner{
		INTupdateProtoManager();
	}
	function updateFeeManager() external onlyOwner{
		INTupdateFeeManager();
	}
	function updateOverseer() external onlyOwner{
		INTupdateOverseer();
	}
//externalChangeALLS-----------------------------------------------------------------------------------------------------------
	function changeTreasury(address payable _account) external onlyOwner{
    		treasury = _account;
    		INTupdateTreasury();
        }
        function changeFeeManager(address _account) external  onlyOwner(){
        	_feeManager = _account;
    		feeMGR = feeManager(_feeManager);
    		INTupdateFeeManager();
        }
        function changeProtoManager(address _account) external  onlyOwner(){
        	_protoManager = _account;
    		protoMGR = protoManager(_protoManager);
    		INTupdateProtoManager();
        }
        function changeOverseer(address _account) external  onlyOwner(){
    		_overseer = _account;
    		over = overseer(_overseer);
    		INTupdateOverseer();
        }
        function changeDropManager(address _account) external  onlyOwner(){
        	_dropManager = _account;
        	dropMGR = dropManager(_dropManager);
        	INTupdateDropManager();
        }
        function changeBoostManager(address _account) external  onlyOwner(){
        	_boostManager = _account;
    		boostMGR = boostManager(_boostManager);
    		INTupdateBoostManager();
        }
        function changeTeamPool(address _account) external onlyOwner(){
        	teamPool = _account;
        	INTupdateTeamPool();
        }
        function changeRewardsPool(address _account) external onlyOwner(){
        	rewardsPool = _account;
        	INTupdateRewardsPool();
        }
//externalChange-----------------------------------------------------------------------------------------------------------
	function changeTreasury(address payable _account) external onlyOwner{
    		treasury = _account;
        }
        function changeFeeManager(address _account) external  onlyOwner(){
        	_feeManager = _account;
    		feeMGR = feeManager(_feeManager);
        }
        function changeProtoManager(address _account) external  onlyOwner(){
        	_protoManager = _account;
    		protoMGR = protoManager(_protoManager);
        }
        function changeOverseer(address _account) external  onlyOwner(){
    		_overseer = _account;
    		over = overseer(_overseer);
        }
        function changeDropManager(address _account) external  onlyOwner(){
        	_dropManager = _account;
        	dropMGR = dropManager(_dropManager);
        }
        function changeBoostManager(address _account) external  onlyOwner(){
        	_boostManager = _account;
    		boostMGR = boostManager(_boostManager);
        }
        function changeTeamPool(address _account) external onlyOwner(){
        	teamPool = _account;
        }
        function changeRewardsPool(address _account) external onlyOwner(){
        	rewardsPool = _account;
        }
//externalGets-----------------------------------------------------------------------------------------------------------
	function getTreasury() external returns(address){
		return treasury;
	}
	function getBoostManager() external returns(address){
		return _boostManager;
	}
	function getDropManager() external returns(address){
		return _dropManager;
	}
	function getProtoManager() external returns(address){
		return _protoManager;
	}
	function getFeeManager() external returns(address){
		return _feeManager;
	}
	function getOverseer() external returns(address){
		return _overseer;
	}
	function getRewardsPool() external returns(address){
		return rewardsPool;
	}
	function getTeamPool() external returns(address){
		return teamPool;
	}
}