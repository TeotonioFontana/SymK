# LB-NOTE-001 --- Uma conversa sobre Teses, Argumentos e Estratégia

**Status:** Nota de reflexão

## Contexto

Durante a validação conceitual do LexBrain surgiu uma pergunta:

> Qual é exatamente o papel do Argumento?

A discussão começou técnica, mas terminou revelando uma importante
separação arquitetônica entre conhecimento e estratégia.

## A conversa

**Duke:** Acho que um argumento existe para apoiar uma tese.

**Teotônio:** Sim, mas não apenas isso. Os argumentos também delimitam o
espaço dos contra-argumentos.

**Duke:** Então eles não apenas aumentam a chance de aceitação da tese.
Eles também reduzem as possibilidades de ataque do adversário.

**Teotônio:** Exatamente. Um processo judicial não é um artigo
científico. Existe um adversário inteligente tentando destruir sua
construção.

Até então nosso modelo era:

    Tese
     ↑
    Argumentos

Mas isso era incompleto.

O argumento possui duas funções:

-   fortalecer a tese;
-   restringir as alternativas estratégicas do adversário.

## O exemplo decisivo

Dois advogados extremamente experientes do mesmo escritório.

### Advogado A

Defende petições iniciais minimalistas.

Argumenta que cada argumento revelado entrega informação ao adversário e
reduz sua liberdade de manobra futura.

### Advogado B

Defende apresentar todos os argumentos possíveis desde a petição
inicial.

Argumenta que isso aumenta o convencimento imediato e reduz o risco de
omissões.

## Quem está certo?

A resposta foi imediata:

> Impossível dizer.

Os dois obtêm excelentes resultados.

Logo, a divergência não está na tese nem nos argumentos.

Ela está na estratégia de utilização desses argumentos.

## A descoberta

O Argumento é um objeto de conhecimento.

A Estratégia é o plano de utilização dos argumentos.

A estratégia responde:

-   quais argumentos utilizar;
-   em que ordem;
-   em que intensidade;
-   em que momento processual;
-   antecipando quais reações do adversário.

Ela manipula argumentos.

Ela não cria argumentos.

## Consequência para o LexBrain

    Tese Jurídica
          │
          ▼
    Argumentos
          │
          ▼
    Repositório de Conhecimento
          │
          ▼
    Estratégia de Utilização
          │
          ▼
    Peça Processual

O LexBrain preserva o conhecimento.

O Redator (ou futuro Composer) define a estratégia de utilização desse
conhecimento.

## Princípio

> Sempre que a estratégia puder variar enquanto o conhecimento permanece
> válido, conhecimento e estratégia devem ser modelados separadamente.

## Reflexão final

Talvez a maior descoberta desta conversa seja que o LexBrain não deve
decidir qual estratégia é correta.

Seu papel é preservar o melhor conjunto possível de teses e argumentos.

A escolha estratégica pertence ao advogado responsável pelo caso.

Em resumo:

> O LexBrain preserva o conhecimento.
>
> O advogado preserva a liberdade estratégica.
