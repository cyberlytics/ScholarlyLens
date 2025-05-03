import React from 'react'
import { Author } from '../apiModels/AuthorsInterface';
import ScholarRankCard from '../components/ScholarRankCard';

interface ScholarsPageProps {
  authors: Author[];
  title?: string; // Optional title prop
}

const ScholarsPage: React.FC<ScholarsPageProps> = ({ authors, title = "Scholars" }) => {

  console.log('authors', authors)
  if (!authors || !Array.isArray(authors)) {
    return <div>Loading scholars...</div>;
  }
  
  return (
    <div>
      <h2>{title}</h2>
      {authors.length === 0 ? (
        <p>No scholars found.</p>
      ) : (
        authors.map((author, idx) => (
          <ScholarRankCard key={author.name + idx} author={author} rank={idx + 1} />
        ))
      )}
    </div>
  )
}

export default ScholarsPage