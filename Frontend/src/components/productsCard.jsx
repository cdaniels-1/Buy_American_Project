import { useEffect, useState } from "react";
import { api } from "../api/client";
import { Link as RouterLink } from "react-router-dom";
import {
    Box,
    Heading,
    Text,
    Stack,
    Card,
    CardHeader,
    CardBody,
    Link as ChakraLink,
    Badge
} from "@chakra-ui/react";

export default function ProductsCard() {
    const [products, setProducts] = useState(null);

    useEffect(() => {
        api.get("/products").then(res => {
            console.log("PRODUCTS DATA:", res.data);
            setProducts(res.data);
        });
    }, []);

    if (!products) return <Text>Loading product list...</Text>;

    return (
        <Box padding="20px">
            <Heading size="lg" mb={4}>Products</Heading>

            <Stack spacing={4}>
                {products.map(product => (
                    <Card key={product.product_id} borderWidth="1px" borderRadius="lg" boxShadow="sm" padding="10px">
                        <CardHeader p={1}>
                            <ChakraLink
                                as={RouterLink}
                                to={`/products/${product.product_id}`}
                                fontSize="xl"
                                fontWeight="bold"
                                color="blue.500"
                            >
                                {product.item_description}
                            </ChakraLink>
                        </CardHeader>

                        <CardBody>
                            <Stack spacing={1} fontSize="sm">
                                <Badge
                                    colorScheme={
                                        product.final_domestic_status === "Domestic"
                                            ? "green"
                                            : product.final_domestic_status === "Foreign"
                                            ? "red"
                                            : "yellow"
                                    }
                                    width="fit-content"
                                    px={2}
                                    py={1}
                                >
                                    {product.final_domestic_status}
                                </Badge>

                                <Text><strong>Product ID:</strong> {product.product_id}</Text>
                                <Text><strong>Brand:</strong> {product.brand}</Text>
                                <Text><strong>Country of Origin:</strong> {product.final_country}</Text>
                                <Text><strong>Sysco Country:</strong> {product.sysco_country}</Text>
                                <Text><strong>Sysco Status:</strong> {product.sysco_domestic_status}</Text>
                                <Text><strong>Multiple Countries:</strong> {product.has_multiple_countries ? "Yes" : "No"}</Text>
                                <Text><strong>Override Country:</strong> {product.override_country || "None"}</Text>
                                <Text><strong>À La Carte:</strong> {product.is_a_la_carte ? "Yes" : "No"}</Text>
                                <Text><strong>Exception Cheaper:</strong> {product.exception_cheaper ? "Yes" : "No"}</Text>
                                <Text><strong>Exception Non-Domestic:</strong> {product.exception_non_domestic ? "Yes" : "No"}</Text>
                                <Text><strong>Manual Override Status:</strong> {product.manual_override_status || "None"}</Text>
                                <Text><strong>Notes:</strong> {product.notes || "None"}</Text>
                            </Stack>
                        </CardBody>
                    </Card>
                ))}
            </Stack>
        </Box>
    );
}
