import { useEffect, useState } from "react";
import { api } from "../api/client";
import { Box, Heading, Text, Stack } from "@chakra-ui/react";

export default function SummaryCard() {
    const [summary, setSummary] = useState(null);

    useEffect(() => {
        api.get("/summary").then(res => {
            console.log("SUMMARY DATA:", res.data);
            setSummary(res.data);
        });
    }, []);

    if (!summary) {
        return <Text>Loading summary...</Text>;
    }

    return (
        <Box
            padding="20px"
            borderWidth="1px"
            borderRadius="lg"
            boxShadow="md"
        >
            <Heading size="lg" mb={4}>Summary</Heading>

            <Heading size="md" mb={2}>Products</Heading>
            <Stack spacing={1} mb={4}>
                <Text>Total Products: {summary.Products.Total}</Text>
                <Text>Domestic Products: {summary.Products.Domestic}</Text>
                <Text>Foreign Products: {summary.Products.Foreign}</Text>
                <Text>Unknown Products: {summary.Products.Unknown}</Text>
            </Stack>

            <Heading size="md" mb={2}>Spending</Heading>
            <Stack spacing={1}>
                <Text>Total Spending: ${summary.Spending.Total}</Text>
                <Text>Domestic Spending: ${summary.Spending.Domestic}</Text>
                <Text>Foreign Spending: ${summary.Spending.Foreign}</Text>
                <Text>Foreign Percentage: {summary.Spending["Foreign percentage"]}%</Text>
                <Text>Domestic Percentage: {summary.Spending["Domestic percentage"]}%</Text>
            </Stack>
        </Box>
    );
}
