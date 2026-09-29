import { useEffect, useState, useRef } from "react";
import { api } from "../api/client";
import {
    Box,
    Text,
    Flex,
    Badge,
    Heading
} from "@chakra-ui/react";
import { useVirtualizer } from "@tanstack/react-virtual";

export default function SpendingRowsDetailsList({ productId }) {
    const [rows, setRows] = useState(null);
    const parentRef = useRef(null);

    useEffect(() => {
        api.get(`/spending-rows/${productId}`).then(res => {
            console.log("DETAIL ROWS:", res.data);
            setRows(res.data);
        });
    }, [productId]);

    if (rows === null) {
        return <Text>Loading...</Text>;
    }

    if (rows.length === 0) {
        return <Text>No spending rows found for product {productId}.</Text>;
    }

    const rowVirtualizer = useVirtualizer({
        count: rows.length,
        getScrollElement: () => parentRef.current,
        estimateSize: () => 90,
        overscan: 10,
    });

    return (
        <Box>
            <Heading size="lg" mb={4}>
                Spending Rows for Product {productId}
            </Heading>

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
                                    <Text><strong>Customer:</strong> {row.customer_name}</Text>
                                    <Text><strong>Obligation:</strong> {row.obligation_number}</Text>
                                    <Text><strong>Date:</strong> {row.obligation_date}</Text>
                                    <Text><strong>Quantity:</strong> {row.quantity}</Text>
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
