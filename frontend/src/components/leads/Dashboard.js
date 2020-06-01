import React, { Fragment } from "react";
import Leads from "./Leads";
import Form from "./Form";

export default function Dashboard() {
  return (
    <div>
      <Fragment>
        <Form />
        <Leads />
      </Fragment>
    </div>
  );
}
