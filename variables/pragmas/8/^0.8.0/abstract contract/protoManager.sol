//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
abstract contract protoManager is Context{
	function updateFeeManager(address _account) external virtual;
	function updateDropManager(address _account) external virtual;
	function updateBoostManager(address _account) external virtual;
	function updateTreasury(address _account) external virtual;
	function updateNeFiToken(address _account) external virtual;
        function updateFeeToken(address _account) external virtual;
}