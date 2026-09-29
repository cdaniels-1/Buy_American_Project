import { useEffect, useState } from "react";
import { api } from "../api/client";
import { useParams } from "react-router-dom";
import {
    Heading,
    Text,
    Stack,
    Badge,
    Card,
    CardHeader,
    CardBody
} from "@chakra-ui/react";

export default function ProductDetailsPage() {
    const { id } = useParams();
    const [product, setProduct] = useState(null);

    useEffect(() => {
        api.get(`/products/${id}`).then(res => {
            if (res.data.error) {
                setProduct("NOT_FOUND");
            } else {
                console.log("PRODUCT DETAILS:", res.data);
                setProduct(res.data);
            }
        });
    }, [id]);

    if (product === "NOT_FOUND") {
        return <Text color="red.500">Product not found.</Text>;
    }

    if (!product) {
        return <Text>Loading product...</Text>;
    }

    return (
        <Card borderWidth="1px" borderRadius="lg" boxShadow="md" padding="10px">
            <CardHeader>
                <Heading size="lg">{product.item_description}</Heading>
            </CardHeader>

            <CardBody>
                <Stack spacing={2}>
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
                    <Text><strong>Sysco Domestic Status:</strong> {product.sysco_domestic_status}</Text>
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
    );
}
