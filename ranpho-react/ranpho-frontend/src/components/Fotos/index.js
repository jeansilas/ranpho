import React from "react";
import { useState } from "react";
import "./index.css";
import axios from "axios";
import "./index.css";


export default function FOTO_ALBUM(props) {
  
  return (
    <div className="contornoImagem">
      <img className="img" alt="Doguinho" src={props.src}/>
    </div>
  );
};