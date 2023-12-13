//SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;
library PuTLib {
		function addressInList(address[] memory _list, address _account) internal pure returns (bool){
			for(uint i=0;i<_list.length;i++){
				if(_account == _list[i]){
					return true;
				}
			}
			return false;
		}
		function mainBalance(address _account) internal view returns (uint256){
			uint256 _balance = _account.balance;
			return _balance;
		}
		function getMultiple(uint256 _x,uint256 _y)internal pure returns(uint256){
			uint256 Zero = 0;
			if (_y == Zero || _x == Zero || _x > _y){
				return Zero;
			}
			uint256 z = _y;
			uint256 i = 0;
			while(z >= _x){
				z -=_x;
				i++;
			}
			return i;
		}
}