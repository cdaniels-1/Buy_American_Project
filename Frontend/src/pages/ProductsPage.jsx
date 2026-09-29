import { useState } from "react"
import { Box, Input } from "@chakra-ui/react"
import ProductsCard from "../components/productsCard";

export default function ProductsPage() {
    const [searchId, setSearchId] = useState("");
    return (
        <Box padding="20px">
            <Input 
                type="number"
                placeholder="Search by product ID"
                value={searchId}
                onChange={(e) => setSearchId(e.target.value)}
                onKeyDown={(e) => {
                    if (e.key === "Enter") {
                        window.location.href = `/products/${e.target.value}`;
                    }
                }}
            />
            <ProductsCard/>
        </Box>
      );
}