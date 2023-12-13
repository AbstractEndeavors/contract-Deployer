//SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;
    using SafeMath for uint;
    struct PROTOstars {
	string name;
	uint256 creationTime;
	uint256 lastClaimTime;
	uint256 protoElapsed;
	uint256 protoLife;
	uint256 lifeDecrease;
	uint256 collapseDate;
	bool insolvent;
    }