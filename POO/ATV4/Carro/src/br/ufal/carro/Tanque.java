package br.ufal.carro;

public class Tanque {

	private int capacidade;
	private int quantidadePresente;

	public Tanque(int capacidade) {
		this.capacidade = capacidade;
		this.quantidadePresente = 0;
	}

	public void abastecer(int quantidade) {
		if(quantidade > (this.capacidade - this.quantidadePresente)){
			quantidade = capacidade - quantidadePresente;
			System.out.println( "Transbordou, cuidado com os fosforos." );
		}
		this.quantidadePresente += quantidade;
	}

	public void usarCombustivel(int quantidade) {
		if( quantidade > this.quantidadePresente ){
			quantidade = this.quantidadePresente;
		}
		this.quantidadePresente -= quantidade;
	}

	public int getQuantidadePresente(){
		return this.quantidadePresente;
	}

}
