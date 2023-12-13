//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
abstract contract feeManager is Context{
	function updateDropManager(address _account) external virtual;
	function updateBoostManager(address _account) external virtual;
	function updateProtoManager(address _account) external virtual;
	function updateTreasury(address payable _account) external virtual;
	function updateTeamPool(address _account) external virtual;
	function updateRewardsPool(address _account) external virtual;
	function updateNeFiToken(address _account) external virtual;
        function updateFeeToken(address _account) external virtual;
}