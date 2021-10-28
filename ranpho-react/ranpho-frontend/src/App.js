import Album from "./components/album";
import Formulario from "./components/search-bar";
import axios from "axios";
import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [imgs, setImgs] = useState([])
  const [resImg, setResImg] = useState([])

  const options = {
    method: 'GET',
    url: 'https://imgur-apiv3.p.rapidapi.com/3/gallery/search/%7Bsort%7D/%7Bwindow%7D/%7Bpage%7D',
    params: {q: 'cat'},
    headers: {
      authorization: 'Bearer fb6021f7fe8869d5b6e00e42d3b517990a2ee225',
      'x-rapidapi-host': 'imgur-apiv3.p.rapidapi.com',
      'x-rapidapi-key': '8458b05074mshb72ebddfd9200dcp106457jsnaf6d3cd33cf6'
    }
  };

  useEffect(() => {
    axios.request(options).then(
      (response) => setResImg(response.data));

      let imgArray = [];
      for (let data in resImg.data) {
        
        let imagem = resImg.data[data].images;
        for (let inf in imagem){
          let linkImg = imagem[inf].link;
        
          console.log(linkImg);
          if (!linkImg.includes('.mp4')){
            imgArray.push(linkImg);
          };
        };
      };
      setImgs(imgArray);
  }, []);
  
  console.log(imgs);

  return (
    <div>
      <div className="Conjunto-Imagens">
      {
        imgs.map(
      (img) => (<Album src={img}></Album>))
      }
      </div>
    </div>
  );
};

export default App;