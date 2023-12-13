//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
abstract contract nebulaMath is Context {
	function EXTisInList(address[] memory _list, address _account) external virtual view returns (uint256);
	function EXTgetDecimals(uint256 _x) external virtual view returns (uint256);
	function EXTelimZero(uint256 _y) external virtual view returns(uint256);
	function EXTdecPercentage(uint256 _x,uint256 perc) external virtual view returns(uint,uint256,uint256);
	function EXTsafeDiv(uint256 _x,uint256 _y) external virtual view returns(uint256,uint256);
	function EXTgetAllMultiple(uint256 _x,uint256 _y)external virtual view returns (uint256,uint256);
	function EXTgetRemainder(uint256 _x,uint256 _y)external virtual view returns(uint256);
	function EXTgetMultiple(uint256 _x,uint256 _y)external virtual view returns (uint256);
	function EXTdoMultiple(uint256 _x,uint256 _y)external virtual view returns (uint256);
	function EXTdoAllMultiple2(uint256 _x,uint256 x_2,uint256 _y,uint256 _z) external virtual view returns (uint256,uint256,uint256);
	function EXTdoAllMultiple(uint256 _x,uint256 _y,uint256 _z) external virtual view returns (uint256,uint256,uint256,uint256);
	function EXTsafeMuls(uint256 _x,uint256 _y)external virtual view returns (uint256);
	function EXTfindInList(address[] memory _ls,address _account)external virtual view returns (uint);
	function EXTisLower(uint256 _x,uint256 _y)external virtual view returns (bool);
	function EXTisHigher(uint256 _x,uint256 _y)external virtual view returns (bool);
	function EXTisEqual(uint256 _x,uint256 _y)external virtual view returns (bool);
	function EXTgetLower(uint256 _x,uint256 _y)external virtual view returns (uint256);
	function EXTgetHigher(uint256 _x,uint256 _y)external virtual view returns (uint256);
}