//SPDX-License-Identifier: (Unlicense)
pragma solidity 0.8.4;
    using IterableMapping for IterableMapping.Map;
    struct NodeEntity {
        string name;
        uint creationTime;
        uint lastClaimTime;
        uint256 amount;
    }