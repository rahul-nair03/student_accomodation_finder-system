import { RouterProvider } from "react-router-dom";
import { createBrowserRouter, useNavigate } from "react-router-dom";
import { LogoSvg } from "./logo";


let recommedHostel = null;


const LandingPage = () => {
  const navigate = useNavigate();
  return (
    <div className="flex flex-col gap-y-8">
      <main className="bg-blue-300 min-h-[550px]">
        <div className="min-h-[500px] grid place-items-center">
          <div className="flex flex-col gap-y-8">
            <div className="grid place-items-center">
              <LogoSvg />
            </div>
           <form onSubmit={async (e) => {
            e.preventDefault();
            const backendUrl = new URL("http://localhost:8080/search");
            backendUrl.searchParams.set("hostelName", `${e.target[0].value.trim()}` );

            const response = await fetch(backendUrl, {method : "POST"});
            const responseInJson = await response.json();

            recommedHostel = responseInJson;      
            navigate("/products");      

           }} className="flex gap-x-3">
            <input type="text" className="w-[500px] px-3 py-2 rounded-md" />
            <button type="submit" className="bg-blue-500 text-white px-3 py-2 rounded-md">Submit</button>
           </form>
          </div>
        </div>
        <div className="flex justify-between">
          <Features text={"24x7"} />
          <Features text={"No Brokerage"} />
          <Features text={"Verified Accounts"} />
        </div>
      </main>

      <section className="px-4">
        <h1 className="text-4xl">About Us</h1>
      </section>
    </div>
  );
};

const Features = ({ text }) => {
  return (
    <h2 className="border-2 border-black rounded-md  text-black bg-orange-300 w-40 grid place-items-center h-[50px]">
      {text}
    </h2>
  );
};


const Products = () => {
  return (
    <div className="flex flex-wrap min-h-screen bg-pink-200">
     {
      recommedHostel ? (recommedHostel.map((hostel) => {
        return <ProductCard key={hostel.hostelName} gender={hostel.gender} price={hostel.price} location={hostel.location} rating={hostel.rating} hostelName={hostel.hostelName} />
      })) : <p>No hostel found</p>
     }
    </div>
  );
};

const ProductCard = ({gender, price, location, rating, hostelName }) => {
  return (
    <div className="p-4 border-2 rounded-md w-[300px] h-[300px] flex flex-col gap-y-3">
      <div className="flex gap-x-2">
        <div>
          <h1>Name: {hostelName}</h1>
          <h3>Gender: {gender}</h3>
          <p>Price: {price} </p>
          <p>Campus: {location}</p>
        </div>
        <div className="flex flex-col items-center">
          <p>Rating</p>
          <h1 className="text-3xl font-bold text-red-800">{rating}</h1>
        </div>
      </div>
    </div>
  );
};

const router = createBrowserRouter([
  {
    path: "/",
    element: <LandingPage />,
  },
  {
    path: "/products",
    element: <Products />,
  },
]);

export const App = () => {
  return <RouterProvider router={router} />;
};
