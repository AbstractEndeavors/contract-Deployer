
async function main() {
  const Greeter = await hre.ethers.getContractFactory("NeFiProtoStarManager");
  const greeter = await Greeter.deploy("0xdfd6fa1d4ec0888480aa4ac21ec82e98b0f5708e","0x529BcAf9DE52D8A65E29C07B8B8389b87BDAE792");
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