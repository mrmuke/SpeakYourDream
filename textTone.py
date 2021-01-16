import requests

headers={
    "x-rapidapi-key": "b34786e198mshac69d114b56dcd0p1a76aejsn1778692afa01",
	"x-rapidapi-host": "twinword-language-scoring.p.rapidapi.com",
	"useQueryString": "true"
}
data={
    "text": "Paragraphs are the building blocks of papers. Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences, a paragraph is half a page long, etc. In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph. A paragraph is defined as “a group of sentences or a single sentence that forms a unit” (Lunsford and Connors 116). Length and appearance do not determine whether a section in a paper is a paragraph. For instance, in some styles of writing, particularly journalistic styles, a paragraph can be just one sentence long. Ultimately, a paragraph is a sentence or group of sentences that support one main idea. In this handout, we will refer to this as the “controlling idea,” because it controls what happens in the rest of the paragraph."
}
response = requests.get("https://twinword-language-scoring.p.rapidapi.com/text/", headers=headers, params=data)

print(response.json())