//SPDX-License-Identifier: (Unlicense)
pragma solidity 0.8.4;
    using SafeMath for uint256;
    using IterableMapping for IterableMapping.Map;
    struct NodeEntity {
        string name;
        uint creationTime;
        uint lastClaimTime;
        uint256 amount;
    }