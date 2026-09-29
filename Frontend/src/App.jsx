import { Routes, Route, Link as RouterLink } from "react-router-dom";
import { Box, HStack, Link as ChakraLink } from "@chakra-ui/react";

import SummaryPage from "./pages/SummaryPage";
import ProductsPage from "./pages/ProductsPage";
import ProductDetailsPage from "./pages/ProductDetailsPage";
import SpendingRowsPage from "./pages/SpendingRowsPage";
import SpendingRowsDetailsPage from "./pages/SpendingRowsDetailsPage";

function App() {
  return (
    <Box padding="20px">
      <HStack spacing="20px" marginBottom="20px">
        <ChakraLink as={RouterLink} to="/summary" fontSize="lg" fontWeight="bold">
          Summary
        </ChakraLink>

        <ChakraLink as={RouterLink} to="/products" fontSize="lg" fontWeight="bold">
          Products
        </ChakraLink>

        <ChakraLink as={RouterLink} to="/spending-rows" fontsize="lg" fontWeight="bold">
          Spending
        </ChakraLink>
      </HStack>

      <Routes>
        <Route path="/summary" element={<SummaryPage />} />
        <Route path="/products" element={<ProductsPage />} />
        <Route path="/products/:id" element={<ProductDetailsPage />} />
        <Route path="/spending-rows" element={<SpendingRowsPage />} />
        <Route path="/spending-rows/:id" element={<SpendingRowsDetailsPage />} />
      </Routes>
    </Box>
  );
}

export default App;
