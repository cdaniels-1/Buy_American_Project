import { useEffect, useState, useRef } from "react";
import { api } from "../api/client";
import {
    Box,
    Heading,
    Text,
    Flex,
    Badge
} from "@chakra-ui/react";
import { useVirtualizer } from "@tanstack/react-virtual";

export default function SpendingRowsCard() {
    const [rows, setRows] = useState([]);

    useEffect(() => {
        api.get("/spending-rows").then(res => {
            console.log("SPENDING ROWS:", res.data);
            setRows(res.data);
        });
    }, []);

    const parentRef = useRef(null);

    const rowVirtualizer = useVirtualizer({
        count: rows.length,
        getScrollElement: () => parentRef.current,
        estimateSize: () => 90, // height of each row
        overscan: 10,
    });

    if (!rows.length) return <Text>Loading spending rows...</Text>;

    return (
        <Box padding="20px">
            <Heading size="lg" mb={4}>Spending</Heading>

            <Box
                ref={parentRef}
                height="600px"
                overflow="auto"
                border="1px solid #e2e8f0"
                borderRadius="md"
            >
                <Box
                    height={rowVirtualizer.getTotalSize()}
                    position="relative"
                >
                    {rowVirtualizer.getVirtualItems().map(virtualRow => {
                        const row = rows[virtualRow.index];

                        return (
                            <Flex
                                key={row.row_id}
                                position="absolute"
                                top={0}
                                left={0}
                                right={0}
                                transform={`translateY(${virtualRow.start}px)`}
                                borderBottom="1px solid #e2e8f0"
                                padding="10px"
                                alignItems="center"
                                gap="20px"
                            >
                                <Box width="80px">
                                    <Text fontWeight="bold">#{row.row_id}</Text>
                                </Box>

                                <Box flex="1">
                                    <Text><strong>Product:</strong> {row.product_id}</Text>
                                    <Text><strong>Customer:</strong> {row.customer_name}</Text>
                                    <Text><strong>Obligation:</strong> {row.obligation_number}</Text>
                                </Box>

                                <Badge colorScheme="blue" fontSize="md">
                                    ${row.net_sales_ext}
                                </Badge>
                            </Flex>
                        );
                    })}
                </Box>
            </Box>
        </Box>
    );
}
