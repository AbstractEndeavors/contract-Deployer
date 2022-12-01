// SPDX-License-Identifier: (Unlicense)
abstract contract prevNebulaNftMint is Context {
	function NFTAccountsLength() external virtual returns(uint256);
	function NFTAccountAddress(uint256 _x) external virtual returns(address);
	function NFTaccountExists(address _account) external virtual returns (bool);
	function NFTaccountData(address _account) external virtual returns(uint256,uint256,uint256,uint256,uint256,uint256,uint256,bool);
}
abstract contract overseer is Context {
   function getFee() external view returns(uint256);
   function getCustomPrice(uint256 _price) external view returns(uint256);
} 
contract nebulaNftMint is Ownable {
    struct TOTALS {
    	    uint256 tier_1;
    	    uint256 tier_2;
    	    uint256 tier_3;
    	    uint256 total;
    	    uint256 totalUSD;
    	    uint256 totalAVAX;
    	    bool full;
    	   }
    mapping(address => TOTALS) public totals;
    address[] public NFTaccounts;
    address[] public NFTtransfered;
    address public nftAddress;
    address public _overseer;
    address Guard;
    uint256 public limit;
    uint256[] public maxSupplies;
    uint256[] public nft_cost;
    overseer public over;
    NebulaNFT public nft;
    constructor(address[] memory addresses,uint256[] memory supplies,uint256[] memory _costs,uint256 _limit) {
    	for(uint i = 0;i<addresses.length;i++){
    		require(addresses[i] != address(0) && addresses[i] != address(this),"your constructor addresses contain either burn or this");
    	}
    	nftAddress = addresses[0];
    	nft = NebulaNFT(nftAddress);
    	_overseer = addresses[1];
    	over = overseer(_overseer);
    	for(uint i=0;i<_costs.length;i++){
    		nft_cost.push(_costs[i]*(10**18));
    	}
    	for(uint i=0;i<_costs.length;i++){
    		maxSupplies.push(supplies[i]);
    	}
    	limit = _limit;
    	
    }
    function getMax(uint256 _num) internal pure returns(bool){
        TOTALS storage house = totals[address(this)];
        if(_num == 0){
    		if(house.tier_1 < maxSupplies[_num]){
    			return false;
    		}
    	}
    	if(_num == 1){
    		if(house.tier_2 < maxSupplies[_num]){
    			return false;
    		}
    	}
    	if(_num == 2){
    		if(house.tier_3 < maxSupplies[_num]){
    			return false;
    		}
    	}
    	return true;
    }
    function mint(uint256 _id) payable external {
    	uint256 num = _id - 1;
    	require(getMax(num) == false,"the totala supply for this tier has already been minted");
    	address _account = msg.sender;
    	uint256 _price = over.getCustomPrice(nft_cost[num]);
    	uint256 _value = msg.value;
    	require(_value >= _price,"you did not send enough to purchase this NFT");
    	uint256 balance = nebuLib.mainBalanceOf(_account);
    	require(balance >= _value,"you do not hold enough to purchase this NFT");
        if (nebuLib.isInList(_account,NFTaccounts) == false){
    		NFTaccounts.push(_account);
    	}
    	
    	require(tot.full != true,"sorry, you already have too many NFT's");
    	if (_id == 1){
	    nft.Pmint(_account,1,1,"0x0");
    	}else if (_id == 2){
	    nft.Pmint(_account,2,1,"0x0");
    	}else if (_id == 3){
	    nft.Pmint(_account,3,1,"0x0");
    	}
    	treasury.transfer(_price);
    	uint256 returnBalance = _value.sub(_price);
    	if(returnBalance > 0){
		payable(_account).transfer(returnBalance);
	}
	updateTotals(_account,_id,1,_price);
    }
    function MGRmint(uint256[] memory _ids,address[] memory _accounts,bool[] _sends,bool[] _records,bool[] _fullOverrrides) external onlyManager(msg.sender) {
    	for(uint i=0;i<_ids.length;i++){
    		uint256 _id = _ids[i];
    		address _account = _accounts[i];
	    	uint256 num = _id - 1;
	    	bool _send = sends[i];
	    	bool _record = _records[i];
	    	TOTALS storage tot = totals[_account];
	    	bool full = tot.full;
	    	if(_fullOverrrides[i] == true){
	    		full = false
	    	}
		if (nebuLib.isInList(_account,NFTaccounts) == false){
	    		NFTaccounts.push(_account);
	    	}
	    	if (full == false && _send[i] == true) {
		    	checkFull(num);
		    	if (_id == 1){
			    nft.Pmint(_account,1,1,"0x0");
		    	}else if (_id == 2){
			    nft.Pmint(_account,2,1,"0x0");
		    	}else if (_id == 3){
			    nft.Pmint(_account,3,1,"0x0");
		    	}
		}
		if (_record == true){
		    	updateTotals(_account,_id,1,);
		}
		
	    }
    }
    function transferAllNFTdata(address prev) external onlyManager(msg.sender) {
    		prevNFTpayable _prev = prevNFTpayable(prev);
    	    	uint256 accts = _prev.NFTAccountsLength();
    	    	for(uint i=0;i<accts;i++){
    	    		address _account = _prev.NFTAccountAddress(i);
    	    		if(nebuLib.isInList(_account,PROTOtransfered) == false){
	    	    		TOTALS storage tots = totals[_account];
	    	    		(uint256 a,uint256 b,uint256 c,uint256 d,uint256 e,uint256 f,uint256 g,bool h)= _prev.NFTaccountData(_account);
	    	    		tots.tier_1 = a;
	    	    		tots.tier_2 = b;
	    	    		tots.tier_3 = c;
	    	    		tots.total =d;
	    	    		tots.totalUSD = e;
	    	    		tots.totalAVAX = f;
	    	    		tots.totalfees = g;
	    	    		tots.full = h;
	    			NFTtransfered.push(_account);
	    		}
	    	}
    }
    function updateTotals(address _account, uint256 _id,uint256 _amount) internal {
    	uint256[3] memory vals = [Zero,Zero,Zero];
    	if(_id != 0){
    		vals[_id-1] = _id;
    	}
    	TOTALS storage tot = totals[_account];
    	tot.tier_1 += vals[0];
    	tot.tier_2 += vals[1];
    	tot.tier_3 += vals[2];
    	if(_id != 0){
        	tot.total += 1;
        }
    	tot.totalUSD += _amount;
    	tot.totalAVAX += msg.value;
	tot.full = false;
	if (fees !=false){
		queryFees(_account);
	}
    	if ((tot.tier_1).add(tot.tier_2).add(tot.tier_3) >= 10){
    		tot.full = true;
    	}
    }
    function changeCostNfts(uint256[3] memory _costs) external onlyOwner{
        nft_cost.length = 0;
    	for(uint i = 0;i<_costs.length;i++){
    		nft_cost.push(_costs[i]*(10**18));
    	}
    }
    function NFTaccountExists(address _account) external returns (bool) {
    	return isInList(_account,NFTaccounts);
    }
    function nftAccountData(address _account) external onlyManager(msg.sender) returns(uint256,uint256,uint256,uint256,uint256,uint256,uint256,bool){
    		TOTALS storage tot = totals[_account];
    		return (tot.tier_1,tot.tier_2,tot.tier_3,tot.total,tot.totalUSD,tot.totalAVAX,tot.totalfees,tot.full);
    	}
    function changeNFTAddress(address _address) external onlyManager(msg.sender) {
    	nftAddress = _address;
    	nft = NebulaNFT(nftAddress);
    }
    function updateManagers(address newVal) external onlyOwner {
    	if(isInList(newVal,Managers) ==false){
        	Managers.push(newVal); //token swap address
        }
    }
    function updateGuard(address _address) external onlyOwner {
        Guard = _address; //token swap address
    }
    function changeGracePeriod(uint256 _days) external onlyOwner {
    	gracePeriod = _days * 1 days;
    }
    function nftAccountsLength() external view returns(uint256){
    	return NFTaccounts.length;
    }
    function nftAddress(uint256 _x) external view returns(address){
    	return NFTaccounts[_x];
    }
    function nftAccountExists(address _account) external returns (bool) {
    	return isInList(_account,NFTaccounts);
    }
}
