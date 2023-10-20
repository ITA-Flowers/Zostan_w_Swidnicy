const handleChange = (e) => {
    // console.log(e.target)
    const { name, value } = e.target;
    setFormValues({...formValues, [name] : value});
    // console.log(formValues)
};