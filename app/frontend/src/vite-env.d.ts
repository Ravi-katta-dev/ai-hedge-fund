/// <reference types="vite/client" />

interface ImportMetaEnv {
	readonly VITE_API_URL?: string;
	readonly MODE: string;
	// add more env variables here if needed
}

interface ImportMeta {
	readonly env: ImportMetaEnv;
}
/// <reference types="vite/client" />
