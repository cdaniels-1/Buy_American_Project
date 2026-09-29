import { useState } from "react";
import { Box, Input } from "@chakra-ui/react";
import SpendingRowsCard from "../components/SpendingRowsCard";

export default function SpendingRowsPage() {
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
                        window.location.href = `/spending-rows/${e.target.value}`;
                    }
                }}
                size="lg"
                variant="filled"
                mb={4}
            />

            <SpendingRowsCard />
        </Box>
    );
}
