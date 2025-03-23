import logo from './logo.svg';
import './App.css';

function App() {
  const [data, setData] = useState({
    id: 0,
    name: "",
    type: "",
  });

  useEffect(() => {
    fetch("/animals/2").then((res) =>
      res.json().then((data) => {
        setdata({
          id: data.id,
          name: data.name,
          type: data.type,
        });
      })
    );
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>{data.name}</p>
      </header>
    </div>
  );
}

export default App;
