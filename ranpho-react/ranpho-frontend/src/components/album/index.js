import React from "react";
import { useEffect, useState } from "react";
import "./index.css";
import axios from "axios";


export default function Foto(props) {
  const [titleAlbum, setTitleAlbum] = useState('');

  const titleChanged = (event) => {
    setTitleAlbum(event.target.value);
  };

  const saveImg = (event) => {
    event.preventDefault();
    axios.post("http://127.0.0.1:8000/api/pics/", {albumTitle:titleAlbum, content:props.src}).then(
        (response) => {
          setTitleAlbum("");
        });
  };

  return (
    <div className="contornoImagem">
      <img className="img" alt="Doguinho" src={props.src}>
      </img>
    
      <form className="forms" onSubmit={saveImg}>
        <input
            className="title-album"
            type="text"
            name="titulo"
            placeholder="Insira um nome"
            value={titleAlbum}
            onChange={titleChanged}
        />
        
        <button className="send-button" type="submit">
          <img className="send" src="/heart.png" alt="enviar"/>
        </button>
      </form>
    </div>
  );
}