//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
abstract contract boostManager is Context{
	function updateFeeManager(address _account) external virtual;
	function updateDropManager(address _account) external virtual;
	function updateProtoManager(address _account) external virtual;
	function updateTreasury(address payable _account) external virtual;
	function updateNeFiToken(address _account) external virtual;
        function updateFeeToken(address _account) external virtual;
}