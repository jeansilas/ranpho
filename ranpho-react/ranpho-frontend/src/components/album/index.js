import React from "react";
import "./index.css";

export default function Album(props) {
  return (
    <div className="contornoImagem">
      <input type="checkbox" id="scales" name="scales">
      </input>
      <img className="img" alt="Doguinho" src={props.src}>
      </img>
    </div>
  );
}