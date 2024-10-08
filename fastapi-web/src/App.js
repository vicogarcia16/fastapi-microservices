import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Products } from './routes/Products';
import { ProductCreate } from './routes/ProductCreate';
import { Order } from './routes/Order';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Products />} />
        <Route path="/create" element={<ProductCreate />} />
        <Route path="/order" element={<Order />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
