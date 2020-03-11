import React from 'react'
import { Container, Row, Col } from 'reactstrap';

import CreatePoll from "../components/CreatePoll"

export default function Homepage() {
    return (
        <Container>
            <Row>
                <Col sm="12" md={{ size: 6, offset: 3 }}>
                    <CreatePoll />
                </Col>
            </Row>
        </Container>
    )
}

const container = {
    width: "60%",
}