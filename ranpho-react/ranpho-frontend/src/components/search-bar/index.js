import React from "react";
import { useEffect, useState } from "react";
import "./index.css";

export default function Formulario(){
  const [titleNote, setTitle] = useState("");
  const [contentNote, setContent] = useState("");
  
  return (
      <form className="form-card">
          <input
          className="form-card-title"
          type="text"
          name="titulo"
          placeholder="Escreva um tema de imagem =)"
          value=""
          onChange=""
          />
          <button className="btn" type="submit">Criar</button>
      </form>
  );
}
