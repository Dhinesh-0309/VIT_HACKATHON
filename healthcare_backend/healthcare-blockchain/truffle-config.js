module.exports = {
  networks: {
    development: {
      host: "127.0.0.1",  // Localhost for Ganache
      port: 7545,         // Default Ganache port
      network_id: "*",    // Match any network
    },
  },
  compilers: {
    solc: {
      version: "0.8.0", // Match Solidity version with your contract
    },
  },
};
