import React, { Fragment } from "react";
import Leads from "./Leads";
import Form from "./Form";
import Header from "../layout/Header";

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
