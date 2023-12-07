//SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;
	using SafeMath for uint256;
		function EXTaddressInList(address[] memory _list, address _account) external view returns (bool){
			return addressInList(_list,_account);
			}