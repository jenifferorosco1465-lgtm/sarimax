import "./globals.css";
export const metadata={title:"SARIMAX Ecuador",description:"Réplica reproducible de inflación y ENSO"};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="es"><body><header><b>SARIMAX Ecuador</b><nav><a href="/">Inicio</a><a href="/resultados">Resultados</a><a href="/metodologia">Metodología</a></nav></header><main>{children}</main><footer>Datos: INEC y NOAA · Código reproducible</footer></body></html>}
