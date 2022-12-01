// SPDX-License-Identifier: (Unlicense)
pragma solidity ^0.8.0;
abstract contract Context {
    function _msgSender() internal view virtual returns (address) {
        return msg.sender;
    }
    function _msgData() internal view virtual returns (bytes calldata) {
        return msg.data;
    }
}
pragma solidity ^0.8.0;
abstract contract Ownable is Context {
    address private _owner;
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    constructor() {
        _transferOwnership(_msgSender());
    }
    modifier onlyOwner() {
        _checkOwner();
        _;
    }
    function owner() public view virtual returns (address) {
        return _owner;
    }
    function _checkOwner() internal view virtual {
        require(owner() == _msgSender(), "Ownable: caller is not the owner");
    }
    function renounceOwnership() public virtual onlyOwner {
        _transferOwnership(address(0));
    }
    function transferOwnership(address newOwner) public virtual onlyOwner {
        require(newOwner != address(0), "Ownable: new owner is the zero address");
        _transferOwnership(newOwner);
    }
    function _transferOwnership(address newOwner) internal virtual {
        address oldOwner = _owner;
        _owner = newOwner;
        emit OwnershipTransferred(oldOwner, newOwner);
    }
}

pragma solidity ^0.8.0;

interface IERC165 {
    
    function supportsInterface(bytes4 interfaceId) external view returns (bool);
}
pragma solidity ^0.8.0;

interface IERC1155 is IERC165 {
    
    event TransferSingle(address indexed operator, address indexed from, address indexed to, uint256 id, uint256 value);
    
    event TransferBatch(
        address indexed operator,
        address indexed from,
        address indexed to,
        uint256[] ids,
        uint256[] values
    );
    
    event ApprovalForAll(address indexed account, address indexed operator, bool approved);
    
    event URI(string value, uint256 indexed id);
    
    function balanceOf(address account, uint256 id) external view returns (uint256);
    
    function balanceOfBatch(address[] calldata accounts, uint256[] calldata ids)
        external
        view
        returns (uint256[] memory);
    
    function setApprovalForAll(address operator, bool approved) external;
    
    function isApprovedForAll(address account, address operator) external view returns (bool);
    
    function safeTransferFrom(
        address from,
        address to,
        uint256 id,
        uint256 amount,
        bytes calldata data
    ) external;
    
    function safeBatchTransferFrom(
        address from,
        address to,
        uint256[] calldata ids,
        uint256[] calldata amounts,
        bytes calldata data
    ) external;
}
library myLib {
	function addressInList(address[] _list, address _account) internaly pure returns(bool){
		for(uint i=0;i<_list.length;i++){
			if(_account == _list[i]{
				return true;
			}
		}
		return false;
	}
	function idInList(address[] _list, uint256 _id) internaly pure returns(bool){
		for(uint i=0;i<_list.length;i++){
			if(_account == _list[i]{
				return true;
			}
		}
		return false;
	}
}
pragma solidity ^0.8.0;

interface IERC1155Receiver is IERC165 {
    
    function onERC1155Received(
        address operator,
        address from,
        uint256 id,
        uint256 value,
        bytes calldata data
    ) external returns (bytes4);
    
    function onERC1155BatchReceived(
        address operator,
        address from,
        uint256[] calldata ids,
        uint256[] calldata values,
        bytes calldata data
    ) external returns (bytes4);
}
pragma solidity ^0.8.0;

abstract contract ERC165 is IERC165 {
    
    function supportsInterface(bytes4 interfaceId) public view virtual override returns (bool) {
        return interfaceId == type(IERC165).interfaceId;
    }
}
pragma solidity ^0.8.0;

abstract contract ERC1155Receiver is ERC165, IERC1155Receiver {
    
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC165, IERC165) returns (bool) {
        return interfaceId == type(IERC1155Receiver).interfaceId || super.supportsInterface(interfaceId);
    }
}
pragma solidity ^0.8.7;
contract nft_stake is Ownable {
    IERC1155 public parentNFT;
    address _NFTcontract = 0x0809174aBA0328E3663476Df3c2E7e0711E40161;
    address public NFTcontract;
    uint256 public time = block.timestamp;
    struct Stake_1 {
        uint256 tokenId;
        uint256 amount;
        uint256[] timestamp;
    }
    struct Stake_2 {
        uint256 tokenId;
        uint256 amount;
        uint256[] timestamp;
    }
    struct Stake_3 {
        uint256 tokenId;
        uint256 amount;
        uint256[] timestamp;
    }

    mapping(address => Stake_1) public stakes_1;
    mapping(address => Stake_2) public stakes_2;
    mapping(address => Stake_3) public stakes_3;
    mapping(address => uint256[]) public stakingTime_1;
    mapping(address => uint256[]) public stakingTime_2;
    mapping(address => uint256[]) public stakingTime_3; 
    address[] public accounts;
    constructor() {
    NFTcontract = _NFTcontract;
    }
    function isStaked(address _account) external view returns(bool){
    	return myLib.isInList(accounts,_account);
    }
    function idAmount(address _account,uint256 i) external view returns(uint256){
      	if (i == 0){
  		return stake_1[_account].length;
  	}
  	if (i == 1){
  		return stake_2[_account].length;
  	}
  	if (i == 2){
  		return stake_3[_account].length;
  	}
    }
    function getTimes(address _account,uint256 i,uint256 k) external view returns(uint256){
      	if (i == 0){
  		return stake_1[_account][k];
  	}
  	if (i == 1){
  		return stake_2[_account][k];
  	}
  	if (i == 2){
  		return stake_3[_account][k];
  	}
    }
    function stake(uint256 _tokenId, uint256 _amount) public {
    	if (_tokenId == 1) {
    		stakes_1[msg.sender].tokenId = 1;
        	stakes_1[msg.sender].amount += _amount;
        	uint j;
		while (j < _amount) {
			stakingTime_1[msg.sender].push(time);
			j++;
		}
        }
        if (_tokenId == 2) {
        	stakes_2[msg.sender].tokenId = 2;
        	stakes_2[msg.sender].amount += _amount;
		uint j;
		while (j < _amount) {
			stakingTime_2[msg.sender].push(time);
			j++;
		}
        }
        if (_tokenId == 3) {
        	stakes_3[msg.sender].tokenId = 3;
        	stakes_3[msg.sender].amount += _amount;
        	uint j;
		while (j < _amount) {
			
			stakingTime_3[msg.sender].push(time);
			j++;
		}
		
        }
       
        parentNFT.safeTransferFrom(msg.sender, address(this), _tokenId, _amount, "0x00");
    } 
    
    function unstake(uint256 _tokenId, uint8 _amount) public {
	    if (_tokenId == 1) {
	    		stakes_1[msg.sender].tokenId = 1;
			stakes_1[msg.sender].amount -= _amount;
			uint j;
			while (j < _amount) {
			    delete stakingTime_1[msg.sender][0];
			    for(uint i = 1;i<stakingTime_1[msg.sender].length;i++){
			    	stakingTime_1[msg.sender][i-1] = stakingTime_1[msg.sender][i];
			    }
			    stakingTime_1[msg.sender].pop();
			    j++;
			}
		}
		if (_tokenId == 2) {
			stakes_2[msg.sender].tokenId = 2;
			stakes_2[msg.sender].amount -= _amount;
			uint j;
			while (j < _amount) {
			    delete stakingTime_2[msg.sender][0];
			    for(uint i = 1;i<stakingTime_2[msg.sender].length;i++){
			    	stakingTime_2[msg.sender][i-1] = stakingTime_2[msg.sender][i];
			    }
			    stakingTime_2[msg.sender].pop();
			    j++;
			}
			
		}
		if (_tokenId == 3) {
			stakes_3[msg.sender].tokenId = 3;
			stakes_3[msg.sender].amount -= _amount;
			uint j;
			while (j < _amount) {
			    delete stakingTime_3[msg.sender][0];
			    for(uint i = 1;i<stakingTime_3[msg.sender].length;i++){
			    	stakingTime_3[msg.sender][i-1] = stakingTime_3[msg.sender][i];
			    }
			    stakingTime_3[msg.sender].pop();
			    j++;
			}
		}
		parentNFT.safeTransferFrom(address(this), msg.sender, _tokenId, _amount, "0x00");
    }  
    
     function onERC1155Received(
        address operator,
        address from,
        uint256 id,
        uint256 value,
        bytes calldata data
    ) external returns (bytes4) {
        return bytes4(keccak256("onERC1155Received(address,address,uint256,uint256,bytes)"));
    }
    function changeNFTcontract(address contract_address) external onlyOwner {
    	NFTcontract = contract_address;
    	parentNFT = IERC1155(NFTcontract);
    }
    
}
