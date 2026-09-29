import { useState } from "react";
import { Box, Input, Text } from "@chakra-ui/react";
import SpendingRowsDetailsList from "../components/SpendingRowsDetailsList";

export default function SpendingRowsDetailsPage() {
    const [productId, setProductId] = useState("");
    const [submittedId, setSubmittedId] = useState(null);

    return (
        <Box padding="20px">
            <Input
                type="number"
                placeholder="Enter product ID"
                value={productId}
                onChange={(e) => setProductId(e.target.value)}
                onKeyDown={(e) => {
                    if (e.key === "Enter") {
                        setSubmittedId(productId);
                    }
                }}
                size="lg"
                variant="filled"
                mb={4}
            />

            {submittedId ? (
                <SpendingRowsDetailsList productId={submittedId} />
            ) : (
                <Text fontSize="lg">Search for a product ID to view spending rows.</Text>
            )}
        </Box>
    );
}
