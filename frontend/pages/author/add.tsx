import React from "react";
import { Formik, Field, Form } from "formik";
import { AuthorSerializer } from '@common/BaseApi';

const AddAuthor = () => {
    return (
        <div>
            <h1>Add Author</h1>
            <Formik
                initialValues={{  } as AuthorSerializer}
                onSubmit={async (values) => {
                    await new Promise((resolve) => setTimeout(resolve, 500));
                    alert(JSON.stringify(values, null, 2));
                }}
            >
                <Form>
                    <Field name="name" type="text" />
                    <Field name="email" type="email" />
                    <button type="submit">Submit</button>
                </Form>
            </Formik>
        </div>
    );
}

export default AddAuthor;
