^^0^^
const hre = require("hardhat");
async function main() {
  const Greeter = await hre.ethers.getContractFactory(^^1^^);
  const greeter = await Greeter.deploy(^^2^^,^^3^^);
  await greeter.deployed();
  console.log("Greeter deployed to:", greeter.address);
}
function link(bytecode, libName, libAddress) {
  let symbol = "__" + libName + "_".repeat(40 - libName.length - 2);
  return bytecode.split(symbol).join(libAddress.toLowerCase().substr(2))
}
main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
