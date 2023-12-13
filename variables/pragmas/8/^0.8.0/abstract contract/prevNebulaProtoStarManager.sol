//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
abstract contract prevNebulaProtoStarManager is Context {
    function getDeadStarsData(address _account, uint256 _x) external  virtual returns(string memory,uint256,uint256,uint256,uint256,uint256,uint256,bool,bool);
    function protoAccountData(address _account, uint256 _x) external virtual returns(string memory,uint256,uint256,uint256,uint256,uint256,uint256,uint256,uint256);
    function protoAccountExists(address _account) external virtual returns (bool);
    function getCollapseDate(address _account,uint256 _x) external virtual view returns(uint256);
    function getdeadStarsLength(address _account) external virtual view returns(uint256);
    function getProtoAccountsLength() external virtual view returns(uint256);
    function getProtoAddress(uint256 _x) external virtual view returns(address);
    function getProtoStarsLength(address _account) external virtual view returns(uint256);
}