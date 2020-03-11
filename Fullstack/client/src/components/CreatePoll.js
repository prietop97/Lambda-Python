import React,{ useState } from 'react';
import { Button, Form, FormGroup, Label, Input, InputGroup, InputGroupAddon } from 'reactstrap';
import {v4 as uuidv4} from "uuid"

const OptionInput = ({id, deleteOption,handleChange}) => {
  return (
    <InputGroup className="mb-1">
      <Input type="text" name={id} onChange={handleChange} option={`option${id}`} placeholder="Enter an option here" />
      <InputGroupAddon addonType="preppend"><Button name={id} onClick={deleteOption} color="danger">X</Button></InputGroupAddon>
    </InputGroup>
  )
}

const CreatePoll = () => {
  const [extraInputs,setExtraInputs] = useState([])
  const [formValue,setFormValue] = useState({
    question: "",
    option1: "",
    option2: ""
  })

  const addOption = (e) => {
    e.preventDefault();
    setExtraInputs([...extraInputs,uuidv4()])
  }

  const deleteOption =  (e) => {
    e.preventDefault();
    setExtraInputs(extraInputs.filter((input) => input !== e.target.name ))
  }

  const handleChange = (e) => {
    e.preventDefault();
    setFormValue({
      ...formValue,
      [e.target.name]: e.target.value
    })
  }

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formValue)
  }


  return (
    <Form>
      <FormGroup>
        <h2>Type your question below</h2>
        <Input type="text" name="question" id="question" onChange={handleChange} placeholder="What is your question?" />
      </FormGroup>
      <FormGroup>
        <Label for="options">Options</Label>
        <InputGroup className="mb-1">
          <Input type="option1" name="option1" id="option1" onChange={handleChange} placeholder="Enter an option here" />
        </InputGroup>
        <InputGroup className="mb-1">
          <Input type="option2" name="option2" id="option2" onChange={handleChange} placeholder="Enter an option here" />
        </InputGroup>
        {extraInputs.map((input) => <OptionInput key={input} handleChange={handleChange} deleteOption={deleteOption} id={input}/>)}
      </FormGroup>
      <Button onClick={addOption} color="primary">Add more options</Button>
      <Button className="ml-2" color="success" onClick={handleSubmit}>Create poll</Button>
    </Form>
  );
}

export default CreatePoll;