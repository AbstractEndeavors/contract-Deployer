//SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;
    using SafeMath for uint;
    struct PROTOstars {
	string name;
    	uint256 calcTime;
    	uint256 boostRewardsMin;
    	uint256 lifeDecrease;
    	uint256 rewards;
	uint256 tempBoost;
	uint256 tempTotRewards;
	uint256 elapsed;
	uint256 boostElapsed;
    }