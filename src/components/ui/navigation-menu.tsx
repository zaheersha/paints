"use client";

import React, { useState } from "react";
import { Menu, X } from "lucide-react";

const Navbar = () => {
  const [open, setOpen] = useState(false);

  return (
    <nav className="w-full bg-white shadow-sm fixed top-0 left-0 z-50">
      <div className="max-w-7xl mx-auto flex items-center justify-between px-6 h-16">
        
        {/* Logo */}
        <a href="/" className="font-bold text-lg">
          Vegam Paints
        </a>

        {/* Desktop Links */}
        <ul className="hidden md:flex space-x-8 font-medium">
          <li><a href="/">Home</a></li>
          <li><a href="/about.html">About</a></li>
          <li><a href="/products.html">Products</a></li>
          <li><a href="/contact.html">Contact</a></li>
        </ul>

        {/* Desktop Button */}
        <a
          href="/contact.html"
          className="hidden md:inline-block bg-black text-white px-4 py-2 rounded-md"
        >
          Get a Quote
        </a>

        {/* Mobile Button */}
        <button
          className="md:hidden"
          onClick={() => setOpen(!open)}
        >
          {open ? <X size={26} /> : <Menu size={26} />}
        </button>
      </div>

      {/* Mobile Menu */}
      {open && (
        <div className="md:hidden bg-white shadow-md border-t">
          <ul className="flex flex-col space-y-4 p-6 font-medium">
            <li><a href="/">Home</a></li>
            <li><a href="/about.html">About</a></li>
            <li><a href="/products.html">Products</a></li>
            <li><a href="/contact.html">Contact</a></li>
            <li>
              <a
                href="/contact.html"
                className="block bg-black text-white px-4 py-2 rounded-md text-center"
              >
                Get a Quote
              </a>
            </li>
          </ul>
        </div>
      )}
    </nav>
  );
};

export default Navbar;