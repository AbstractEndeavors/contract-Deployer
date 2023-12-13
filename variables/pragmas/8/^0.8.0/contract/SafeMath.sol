//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
    using SafeMath for uint;
    struct PROTOstars {
	string name;
	uint256 creationTime;
	uint256 lastClaimTime;
	uint256 lifeDecrease;
	uint256 protoElapsed;
	uint256 collapseDate;
	bool insolvent;
	bool imploded;
	bool collapsed;
    }