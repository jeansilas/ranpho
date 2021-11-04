import React from "react";
import "./index.css";

export default function Foto(props) {
  return (
    <div className="contornoImagem">
      <img className="img" alt="Doguinho" src={props.src}>
      </img>
    
      <div className="forms">
        <input
            className="title-album"
            type="text"
            name="titulo"
            placeholder=""
            value=""
            onChange=""
        />
        
        <button className="send-button" type="submit">
          <img className="send" src="/heart.png" alt="enviar"/>
        </button>
      </div>
    </div>
  );
}