import '../styles/globals.css'
import { createTheme, NextUIProvider, defaultTheme } from "@nextui-org/react"
import { getDefaultProvider } from "ethers"
import { WagmiConfig, createClient, } from 'wagmi';

const theme = createTheme({
  type: "dark", // it could be "light" or "dark"
  theme: defaultTheme[0],
});
const client = createClient({
  autoConnect: true,
  provider: getDefaultProvider("goerli"),
});


function MyApp({ Component, pageProps }) {
  return <NextUIProvider theme={theme}>
    <WagmiConfig client={client}>
      <Component {...pageProps} />
    </WagmiConfig>
  </NextUIProvider>
}

export default MyApp
