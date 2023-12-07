//SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;
interface IERC20Metadata is IERC20 {
    function name() external view returns (string memory);
    function symbol() external view returns (string memory);
    function decimals() external view returns (uint8);
}